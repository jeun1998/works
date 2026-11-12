import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

def setScatterGraph(tour_table, all_table, tourPoint):
    print('관광지명 : ', tourPoint)
    print('tour_table 크기 : ', tour_table.shape)
    print('all_table 크기 : ', all_table.shape)

    tour = tour_table[tour_table['resNm'] == tourPoint]
    # print('관광지 방문 데이터 건수 : ', len(tour))
    # print('외국인 방문 데이터 건수 : ', len(all_table))

    merge_table = pd.merge(tour, all_table, left_index=True, right_index=True)
    print(merge_table)

    fig = plt.figure()
    fig.suptitle(tourPoint + '상관관계 분석')

    plt.subplot(1, 3, 1)
    plt.xlabel('중국인 방문수')
    plt.ylabel('외국인 입장객 수')
    lamb1 = lambda p:merge_table['china'].corr(merge_table['ForNum'])
    r1 = lamb1(merge_table)
    print('r1 : ', r1)
    plt.title('r={:.5f}'.format(r1))
    plt.scatter(merge_table['china'], merge_table['ForNum'], alpha=0.7, s=6, c='yellow')

    plt.subplot(1, 3, 2)
    plt.xlabel('일본인 방문수')
    plt.ylabel('외국인 입장객 수')
    lamb2 = lambda p:merge_table['japan'].corr(merge_table['ForNum'])
    r2 = lamb2(merge_table)
    print('r2 : ', r2)
    plt.title('r={:.5f}'.format(r2))
    plt.scatter(merge_table['japan'], merge_table['ForNum'], alpha=0.7, s=6, c='red')

    plt.subplot(1, 3, 3)
    plt.xlabel('미국인 방문수')
    plt.ylabel('외국인 입장객 수')
    lamb3 = lambda p:merge_table['usa'].corr(merge_table['ForNum'])
    r3 = lamb3(merge_table)
    print('r3 : ', r3)
    plt.title('r={:.5f}'.format(r3))
    plt.scatter(merge_table['usa'], merge_table['ForNum'], alpha=0.7, s=6, c='blue')

    plt.tight_layout()
    plt.show()
    return [tourPoint, r1, r2, r3]

def processFunc():
    fname = "서울특별시_관광지입장정보_2011_2016.json"
    jsonTP = json.loads(open(fname, mode='r', encoding='utf-8').read())
    # print(jsonTP)
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm', 'resNm', 'ForNum'))
    tour_table = tour_table.set_index('yyyymm')
    # print(tour_table.head())
    resNm = tour_table.resNm.unique()
    # print(resNm[:5])
    print(tour_table[:2])

    cdf = '중국인방문객.json'
    jdata = json.loads(open(cdf, mode='r', encoding='utf-8').read())
    china_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    print(china_table[:2])

    cdf = '일본인방문객.json'
    jdata = json.loads(open(cdf, mode='r', encoding='utf-8').read())
    japan_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    print(japan_table[:2])
    
    cdf = '미국인방문객.json'
    jdata = json.loads(open(cdf, mode='r', encoding='utf-8').read())
    usa_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    print(usa_table[:2])

    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(usa_table, all_table, left_index=True, right_index=True)
    # print(all_table)

    r_list = []
    for tourPoint in resNm[:5]:
        r_list.append(setScatterGraph(tour_table, all_table, tourPoint))
    r_df = pd.DataFrame(r_list, columns=('고궁명', '중국', '일본', '미국'))
    r_df = r_df.set_index('고궁명')
    print(r_df)

    r_df.plot(kind='bar', rot=50)
    plt.show()



if __name__ == "__main__":
    processFunc()
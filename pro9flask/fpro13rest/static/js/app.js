// 함수(화살표 함수) 객체 생성 후 $에 할당
const aa = (sel) => document.querySelector(sel);
//function aa(sel){
//    return
//}
// ex)$("sendBtn")하면 return document.querySelector(sel); 가 실행

$("sendBtn").addEventListener("click", async() => { // 비동기 처리
    const name = $("#name").value.trim();
    // const name = document.querySelector("#name").value.trim(); 위와 동일
    // console.log("name", name);
    const age = $("#age").value.trim();
    const params = new URLSearchParams({name, age});
    const url = `/api/friend?{params.toString()}`;
    //console.log(url);
    
    $("#result").textContent = "요청 중 ...";  // 서버에 자료요청 시간이 길어지면 보이는 메세지

    try{
        const res = await fetch(url, {
            method:"GET",
            headers:{"Accept":"application/json"}
        });

        const data = await res.json();
        // alert(data);

        if(!res.ok || data.ok === false){
            $("#result").innerHTML = `<span class="error">에러 : ${data.error}</span>`;
        }

        // 요청 성공인 경우
        $("#result").innerHTML = `
            <div>이름 : ${data.name}</div>
            <div>나이 : ${data.age}</div>
            <div>연령대 : ${data.age_group}</div>
            <div>메세지 : ${data.message}</div>
            
        `;

    }catch(err){
        $("#result").innerHTML = `<span class="error">네트워크 피싱오류 : ${err}</span>`;
    }
})
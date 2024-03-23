console.log('Script Loaded!');
function loadDoc(url, func){
    let xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        if (xhttp.status != 200){
            console.log("Error");
        }
        else{
            func(xhttp.response);
        }
    }
    xhttp.open("GET",url);
    xhttp.send();
}

function course_search(){
    let txtSearch = document.getElementById("txtSearch");
    let url = "/catalog/" + txtSearch.value;
    loadDoc(url, course_search_results);
}

function course_search_results(response){
    let data = JSON.parse(response);
    let result = data["result"];
    let temp = "";

    for (let i = 0; i < result.length; i++){
        let course = result[i];

        temp += "<div class=\"course_container\">";
        temp += "<a href=\"/course/" + course["number"] + "\">" + course["number"] + "</a> :" + course["name"];
        temp += "</div>";

    }

    let divResults = document.getElementById("divResults");
    divResults.innerHTML = temp;

}


function list_files(){
    let url = "/listfiles";
    loadDoc(url, list_files_response);

}

function list_files_response(response){
    console.log(response);

    let data = JSON.parse(response);
    let items = data["items"];
    let url = data["url"];

    let temp = "";
    for (let i = 0; i < items.length; i++){
        temp += "<a href=\""+ url + "/" + items[i] + "\">" + items[i] + "</a><br/>";
    }

    let divResults = document.getElementById("divResults");
    divResults.innerHTML = temp;
}

function filterApts(){
    let search = document.getElementById("search");
    let bedrooms = document.getElementById("bedrooms");
    let sort = document.getElementById("sort");
    let url = "/aptsearch/" + search.value + "/" +bedrooms.value + "/" + sort.value;
    console.log(url);
    loadDoc(url, apt_search_results);

}

function apt_search_results(response){
    console.log(response);
    let data = JSON.parse(response);
    let result = data["result"];

    let temp = "";

    for (let i = 0; i < result.length; i++){
        let apt = result[i];

        temp += "<div class=\"course_container\">";
        temp +=  apt["title"] + ":" + apt["bedrooms"] + ", $" + apt["rent"] + "<br>";
        temp += apt["description"];
        temp += "</div>";
    }
    let divResults = document.getElementById("divResults");
    divResults.innerHTML = temp;
}
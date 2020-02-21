
let url = new URL(document.URL);
let myForm = document.getElementById("my-form").elements;
let postData={};

//delete last params
let queryString = window.location.search;
let urlParams = new URLSearchParams(queryString);
let keys = urlParams.keys();
for (let key of keys) url.searchParams.delete(key);


// Get params and run to new url
document.getElementById("main_button").addEventListener("click", function(event){
document.getElementById("my-form").submit();
event.preventDefault();
for (var i=0; i<myForm.length; i++) {
  if (myForm[i].name && myForm[i].value && myForm[i].value!='All')
    url.searchParams.set(myForm[i].name, myForm[i].value);
    // postData[myForm[i].name] = myForm[i].value;
}
window.location = url;
});

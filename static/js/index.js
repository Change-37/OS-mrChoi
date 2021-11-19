var oScript = document.createElement("script");
oScript.type = "text/javascript";
oScript.src = "//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js";
document.getElementsByTagName("head")[0].appendChild(oScript);

var clicklogo = document.querySelector("#logo");

clicklogo.addEventListener("click", function() {
            $.ajax({
                type: 'GET',
                url:'/insertdb',
                datatype:'json',
                success: function(data) {
                    alert(data)

                    var time = new Date()
                    var tdata = "<tr>"
                    obj = JSON.parse(data)

                    tdata += "<th>1</th>"
                    tdata += "<th>"+time.getFullYear()+"-"+(time.getMonth()+1)+"-"+time.getDate()+"</th>"
                    tdata += "<th>"+time.getHours()+":"+time.getMinutes()+"</th>"
                    tdata += "</tr>"
                    document.getElementById("image").innerHTML = tdata
                }
        });
});
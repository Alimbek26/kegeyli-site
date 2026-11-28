window.goatcounter={path:function(p){return p.replace(/^\/(en|uz|ru)(\/|$)/,"/")||"/"}};
(function(){var C="alimbek26";if(!C)return;var p=location.pathname.replace(/index\.html$/,"").replace(/^\/(en|uz|ru)(\/|$)/,"/")||"/";
function get(x,id){return fetch("https://"+C+".goatcounter.com/counter/"+encodeURIComponent(x)+".json").then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(j){document.getElementById(id).textContent=j.count;return 1})}
if(!/^(localhost|127\.)/.test(location.hostname))Promise.all([get(p,"gcp").catch(function(){document.getElementById("gcp").textContent="—";return 0}),get("TOTAL","gct").catch(function(){return 0})]).then(function(r){if(r[0]||r[1])document.getElementById("gcv").hidden=false})})();

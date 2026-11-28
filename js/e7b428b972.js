(function(){
 var $=function(i){return document.getElementById(i)},K='abroadApps',D=JSON.parse($('abdata').textContent);
 var apps=[];try{apps=JSON.parse(localStorage.getItem(K)||'[]')}catch(e){}
 var save=function(){try{localStorage.setItem(K,JSON.stringify(apps))}catch(e){}};
 var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
 function days(d){var t=new Date();t.setHours(0,0,0,0);return Math.round((new Date(d+'T00:00:00')-t)/864e5)}
 function draw(){
  $('ablist').innerHTML=apps.length?apps.map(function(a,i){
   var n=days(a.d),cls=n<0?'past':n<=14?'soon':'',txt=isNaN(n)?'':(n<0?D.past:n===0?D.today:D.days.replace('{n}',n));
   var done=a.c.filter(Boolean).length;
   return '<div class="card abapp '+cls+'"><div class="abtop"><div><b>'+esc(a.u)+'</b><small>'+esc(a.k||'')+(a.d?' · '+a.d:'')+'</small></div><span class="abdays">'+txt+'</span></div>'
    +'<div class="pbar" style="--sc:#0b5f78"><i style="width:'+Math.round(done/D.docs.length*100)+'%"></i></div><small>'+done+'/'+D.docs.length+' '+D.done+'</small>'
    +'<div class="abdocs">'+D.docs.map(function(x,j){return '<label><input type="checkbox" data-i="'+i+'" data-j="'+j+'"'+(a.c[j]?' checked':'')+'> '+esc(x)+'</label>'}).join('')+'</div>'
    +'<button type="button" class="abdel" data-i="'+i+'">'+D.del+'</button></div>'}).join(''):'<p class="note">'+D.empty+'</p>';
 }
 $('ablist').addEventListener('change',function(e){var t=e.target;if(t.type==='checkbox'){apps[+t.dataset.i].c[+t.dataset.j]=t.checked;save();draw()}});
 $('ablist').addEventListener('click',function(e){var t=e.target;if(t.classList.contains('abdel')){apps.splice(+t.dataset.i,1);save();draw()}});
 $('abform').addEventListener('submit',function(e){e.preventDefault();var u=$('abu').value.trim();if(!u)return;
  apps.push({u:u,k:$('abk').value.trim(),d:$('abd').value,c:D.docs.map(function(){return false})});apps.sort(function(a,b){return (a.d||'9')<(b.d||'9')?-1:1});save();this.reset();draw()});
 draw();
})();

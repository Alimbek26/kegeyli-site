(function(){
 var $=function(id){return document.getElementById(id)};
 var LT=[[39,9],[37,8.5],[35,8],[32,7.5],[30,7],[26,6.5],[23,6],[18,5.5],[16,5],[13,4.5],[10,4],[8,3.5],[6,3],[4,2.5],[0,2]];
 var RT=[[39,9],[37,8.5],[35,8],[33,7.5],[30,7],[27,6.5],[23,6],[19,5.5],[15,5],[13,4.5],[10,4],[8,3.5],[6,3],[4,2.5],[0,2]];
 var band=function(n,t){for(var i=0;i<t.length;i++)if(n>=t[i][0])return t[i][1];return 0};
 var D=JSON.parse($('ieltsdata').textContent);
 var fmt=function(x){return (Math.round(x*2)/2).toFixed(1).replace('.',D.dec)};
 function calc(){
  var l=Math.max(0,Math.min(40,+$('il').value||0)),r=Math.max(0,Math.min(40,+$('ir').value||0));
  var w=+$('iw').value,s=+$('is').value,t=+$('it').value;
  var b=[['L',band(l,LT)],['R',band(r,RT)],['W',w],['S',s]];
  var avg=(b[0][1]+b[1][1]+b[2][1]+b[3][1])/4,ov=Math.floor(avg*2+0.5)/2;
  $('ibands').innerHTML=b.map(function(x){return '<div class="ibt'+(x[1]<t?' low':'')+'"><span>'+D.n[x[0]]+'</span><b>'+fmt(x[1])+'</b></div>'}).join('');
  $('iov').textContent=fmt(ov);
  var low=b.filter(function(x){return x[1]<t}).sort(function(a,c){return a[1]-c[1]});
  $('imsg').textContent=ov>=t?D.reached:D.below.replace('{d}',fmt(t-ov))+(low.length?' · '+D.focus.replace('{s}',low.map(function(x){return D.n[x[0]]}).join(', ')):'');
  $('iresult').className='iresult '+(ov>=t?'ok':'');
  try{localStorage.setItem('ielts',JSON.stringify({l:l,r:r,w:w,s:s,t:t}))}catch(e){}
 }
 try{var sv=JSON.parse(localStorage.getItem('ielts')||'null');if(sv){$('il').value=sv.l;$('ir').value=sv.r;$('iw').value=sv.w;$('is').value=sv.s;$('it').value=sv.t}}catch(e){}
 ['il','ir','iw','is','it'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
 calc();
 var d=new Date(),k=Math.floor((d-new Date(d.getFullYear(),0,0))/864e5)%D.w;
 document.querySelectorAll('.iword').forEach(function(e){e.hidden=+e.dataset.k!==k});
})();

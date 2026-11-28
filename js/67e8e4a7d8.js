(function(){var C=window.CAL,t=C.t,P=new URLSearchParams(location.search).get('d'),
today=/^\d{4}-\d\d-\d\d$/.test(P||'')?P:new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Tashkent'}).format(new Date());
function dd(a,b){return Math.round((Date.parse(b)-Date.parse(a))/864e5)}
function f(s,o){return s.replace(/\{(\w)\}/g,function(m,k){return o[k]})}
var $=function(i){return document.getElementById(i)},S=C.school,first=C.terms[0][1],last=C.terms[3][2],card=$('cnow');
var cur=null,brk=null,nextT=null;C.terms.forEach(function(x){if(today>=x[1]&&today<=x[2])cur=x;if(!nextT&&x[1]>today)nextT=x});
C.breaks.forEach(function(x){if(today>=x[1]&&today<=x[2])brk=x});
var isLesson=S.indexOf(today)>=0,done=S.filter(function(d){return d<=today}).length;
function big(n,small){$('cnc').innerHTML='<b>'+n+'</b><span>'+t.dl+'</span><small>'+small+'</small>'}
$('cnk').textContent=t.today+' · '+(C.dates[today]||today)+(cur&&!isLesson?' · '+t.dayoff:'');
if(cur){card.style.setProperty('--tc',cur[5]);$('cnh').textContent=cur[3];
 var n=S.filter(function(d){return d>=cur[1]&&d<=today}).length;$('cnb').style.width=(n/cur[4]*100)+'%';$('cnp').textContent=f(t.prog,{a:n,b:cur[4]});
 var nb=C.breaks.filter(function(x){return x[1]>today})[0];
 if(nb){var lft=S.filter(function(d){return d>today&&d<nb[1]}).length;big(dd(today,nb[1]),nb[4]+' · '+(lft||!isLesson?f(t.left_l,{n:lft}):t.lastday))}}
else if(today<first){$('cnh').textContent=C.terms[0][3];big(dd(today,first),f(t.before,{d:C.dates[first]}));$('cnb').style.width='0';}
else if(brk&&nextT){card.classList.add('onbreak');$('cnh').textContent=brk[3];big(dd(today,nextT[1]),f(t.resume,{d:C.dates[nextT[1]]}));
 $('cnb').style.width=(dd(brk[1],today)+1)/(dd(brk[1],brk[2])+1)*100+'%';$('cnp').textContent=nextT[3]+' · '+C.dates[nextT[1]];}
else{card.classList.add('onbreak');$('cnh').textContent=brk?brk[3]:'';$('cnc').innerHTML='<span class="cover">'+t.over+'</span>';$('cnb').style.width='100%';$('cnp').textContent='';}
$('cnd').textContent=f(t.year_done,{p:Math.min(100,Math.round(done/S.length*100))});$('cny').style.width=Math.min(100,done/S.length*100)+'%';
var tl=document.querySelector('.ctl'),k=dd(tl.dataset.a,today)/(+tl.dataset.n)*100;if(k>=0&&k<=100){var m=document.querySelector('.ctlnow');m.style.left=k+'%';m.hidden=false}
document.querySelectorAll('.cterm[data-a]').forEach(function(b){var s=b.querySelector('.cst');s.hidden=false;
 if(today>b.dataset.b){s.textContent='✓ '+t.st_done;b.classList.add('done')}else if(today>=b.dataset.a){s.textContent=t.st_now;b.classList.add('now')}else{s.textContent=t.st_next}});
document.querySelectorAll('.cbr').forEach(function(r){if(today>r.dataset.b)r.classList.add('past');else if(today>=r.dataset.a)r.classList.add('now')});
var tc=document.querySelector('.cd[data-d="'+today+'"]');if(tc){tc.classList.add('today');tc.setAttribute('aria-current','date')}
var info=$('cinfo'),sel=null;function close(){if(sel)sel.classList.remove('sel');sel=null;info.hidden=true}
document.querySelectorAll('.cgrid .cd').forEach(function(c){c.addEventListener('click',function(e){e.stopPropagation();if(sel===c){close();return}
 if(sel)sel.classList.remove('sel');sel=c;c.classList.add('sel');info.querySelector('span').textContent=c.dataset.i;info.hidden=false})});
info.querySelector('button').addEventListener('click',close);document.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
document.addEventListener('click',function(e){if(sel&&!info.contains(e.target))close()});
var bs=document.querySelectorAll('.cterm');function filt(v,scroll){bs.forEach(function(x){x.classList.toggle('on',x.dataset.t===v)});
 document.querySelectorAll('.cmon').forEach(function(m){m.hidden=v!=='all'&&m.dataset.t.split(' ').indexOf(v)<0});close();
 if(scroll)$('cmh').scrollIntoView({behavior:'smooth',block:'start'})}
bs.forEach(function(b){b.addEventListener('click',function(){filt(b.dataset.t,b.dataset.t!=='all')})});
document.querySelectorAll('.ctl .tl[data-t]').forEach(function(x){x.addEventListener('click',function(){filt(x.dataset.t,true)})});
$('csem').addEventListener('change',function(e){$('cmonths').classList.toggle('nosem',!e.target.checked)});
})();

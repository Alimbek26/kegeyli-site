(function(){var t=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Tashkent'}).format(new Date());
var up=document.getElementById('smup'),pa=document.getElementById('smpast');
[].slice.call(up.children).forEach(function(r){if(r.dataset.d<t||r.dataset.done){pa.insertBefore(r,pa.firstChild)}});
document.querySelectorAll('.smrow,.smnext').forEach(function(r){if(r.dataset.d===t)r.querySelectorAll('.smtoday').forEach(function(x){x.hidden=false})});
var n=null;document.querySelectorAll('.smnext').forEach(function(c){var ok=!n&&c.dataset.d>=t&&!c.dataset.done;if(ok)n=c;c.hidden=!ok});
document.getElementById('smh').textContent=pa.children.length;document.getElementById('smu').textContent=up.children.length;
document.getElementById('smuph').hidden=!up.children.length;document.getElementById('smpasth').hidden=!pa.children.length;
var cs=document.querySelectorAll('.smchips .chip'),run=function(k){var v=0;document.querySelectorAll('.smrow').forEach(function(r){var ok=k==='all'||r.dataset.s===k;r.hidden=!ok;if(ok)v++});document.getElementById('smnone').hidden=v>0};
cs.forEach(function(b){b.addEventListener('click',function(){cs.forEach(function(x){x.classList.toggle('on',x===b)});run(b.dataset.s)})})})();

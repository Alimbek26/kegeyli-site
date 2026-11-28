{
  const q=document.getElementById('tq');
  if(q){
    const cs=[...document.querySelectorAll('.tcard')],none=document.getElementById('tnone');let sub='all';
    const run=()=>{const v=(q.value||'').trim().toLowerCase();let n=0;for(const c of cs){const ok=(sub==='all'||c.dataset.s===sub)&&(!v||c.dataset.n.includes(v));c.hidden=!ok;if(ok)n++}none.hidden=n>0};
    document.querySelectorAll('.chip').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x===b));sub=b.dataset.s;run()}));
    q.addEventListener('input',run);
  }


  const td=document.getElementById('ttdata');
  if(td){
    const D=JSON.parse(td.textContent),C=D.c,S=D.s,X=D.t,B=D.b,IC=D.ic||{},K=['mon','tue','wed','thu','fri'];
    const $=id=>document.getElementById(id),esc=s=>String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
    const mm=s=>{const[h,m]=s.split(':');return +h*60+ +m};
    const now=()=>{const p={};new Intl.DateTimeFormat('en-US',{timeZone:'Asia/Samarkand',weekday:'long',hour:'2-digit',minute:'2-digit',second:'2-digit',hourCycle:'h23'}).formatToParts(new Date()).forEach(x=>p[x.type]=x.value);return {wd:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(String(p.weekday).slice(0,3)),h:+p.hour,m:+p.minute,s:+p.second}};
    const subj=k=>S[k]||[k,'#0b5f78'];
    // teacher index
    const TI={},TS={};
    for(const c in C)for(const k of K)for(const p in (C[c][k]||{}))for(const [s,t] of C[c][k][p]){if(!t)continue;((TI[t]=TI[t]||{})[k]=TI[t][k]||{})[p]=[c,s];TS[t]=TS[t]||s}
    const tnames=Object.keys(TI).sort((a,b)=>a.localeCompare(b));
    const slug=t=>'t-'+t.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/-+$/,'');
    // select options grouped by subject
    const groups={};tnames.forEach(t=>(groups[TS[t]]=groups[TS[t]]||[]).push(t));
    $('tsel').innerHTML=`<option value="">${X.pickt}</option>`+Object.keys(groups).sort((a,b)=>subj(a)[0].localeCompare(subj(b)[0])).map(g=>`<optgroup label="${esc(subj(g)[0])}">`+groups[g].map(t=>`<option value="${esc(t)}">${esc(t)}</option>`).join('')+'</optgroup>').join('');
    const N0=now(),today=N0.wd<=4?N0.wd:-1,tomorrow=N0.wd>=4?0:N0.wd+1;
    let day=today<0?0:today,view='day',mode='class',cls=null,tch=null;
    {const qt=document.querySelector('#quick [data-q=today]'),qm=document.querySelector('#quick [data-q=tom]');qt.dataset.d=today;qt.hidden=today<0;qm.dataset.d=tomorrow;}
    try{cls=localStorage.getItem('ttcls');tch=localStorage.getItem('tttch');mode=localStorage.getItem('ttmode')||'class'}catch(e){}
    const h=(location.hash||'').slice(1);
    if(h==='free')mode='free';
    else if(C[h.toUpperCase()]){cls=h.toUpperCase();mode='class'}
    else if(h.startsWith('t-')){const f=tnames.find(t=>slug(t)===h);if(f){tch=f;mode='teacher'}}
    if(!C[cls])cls=null;if(!TI[tch])tch=null;
    const sel=()=>mode==='class'?cls:tch;
    // free-teacher state: default = current (or next) period today
    const fsel=new Set();let fsub='';
    {const n=now(),cur=n.h*60+n.m;let p0=B.findIndex(b=>cur<mm(b[1]));if(p0<0||today<0)p0=0;fsel.add(p0+1)}
    $('fper').innerHTML=B.map((b,k)=>`<button type="button" data-p="${k+1}"><b>${k+1}</b><small>${b[0]}</small></button>`).join('')+`<button type="button" data-p="all" class="fall">${X.allday}</button>`;
    $('fsub').innerHTML=`<option value="">${X.fsubj}</option>`+[...new Set(Object.values(TS))].sort((a,b)=>subj(a)[0].localeCompare(subj(b)[0])).map(s=>`<option value="${esc(s)}">${esc(subj(s)[0])}</option>`).join('');
    function renderFree(){
      const k=K[day],ps=[...fsel].sort((a,b)=>a-b);
      document.querySelectorAll('#fper button').forEach(b=>b.classList.toggle('on',b.dataset.p==='all'?fsel.size===B.length:fsel.has(+b.dataset.p)));
      $('ttcls').textContent=X.m_free;
      $('ttcount').textContent=X.days[day]+(ps.length?' · '+ps.map(p=>p).join(', ')+' ('+B[ps[0]-1][0]+' – '+B[ps[ps.length-1]-1][1]+')':'');
      if(!ps.length){$('fres').innerHTML=`<p class="note">${X.pickp}</p>`;return}
      const busy=[],off=[];
      for(const t of tnames){if(fsub&&TS[t]!==fsub)continue;const L=(TI[t][k]||{}),n=Object.keys(L).length;
        if(ps.some(p=>L[p]))continue;
        const after=Object.keys(L).map(Number).filter(p=>p>ps[ps.length-1]).sort((a,b)=>a-b)[0];
        (n?busy:off).push({t,n,nx:after?X.nextl.replace('{p}',after).replace('{c}',L[after][0]):''})}
      const card=o=>`<li style="--sc:${subj(TS[o.t])[1]}"><span class="fav">${esc(o.t.split(' ').map(w=>w[0]).join('').slice(0,2))}</span><div><b>${esc(o.t)}</b><small>${esc(subj(TS[o.t])[0])}${o.n?' · '+X.l_day.replace('{n}',o.n):''}${o.nx?' · '+esc(o.nx):''}</small></div></li>`;
      let out=`<p class="fcount">${X.free_n.replace('{n}',busy.length+off.length)}</p>`;
      if(!busy.length&&!off.length)out=`<p class="note">${X.nonef}</p>`;
      if(busy.length)out+=`<h4>${X.teach_day}</h4><ul class="flist">${busy.map(card).join('')}</ul>`;
      if(off.length)out+=`<details${busy.length?'':' open'}><summary>${X.no_day} (${off.length})</summary><ul class="flist dim">${off.map(card).join('')}</ul></details>`;
      $('fres').innerHTML=out}
    // lessons of the selected class/teacher on day index d: {p:{name,col,sub}}
    function les(d){const k=K[d],o={};
      if(mode==='class'&&cls){const L=(C[cls][k]||{});for(const p in L){const l=L[p],s=subj(l[0][0]),t=l.map(x=>x[1]).filter(Boolean);o[p]={name:s[0],col:s[1],sub:t.join(' · ')+(l.length>1?' — '+X.groups:'')}}}
      if(mode==='teacher'&&tch){const L=(TI[tch][k]||{});for(const p in L){const [c,sb]=L[p],s=subj(sb);o[p]={name:c+' '+X.cls,col:s[1],sub:s[0]}}}
      return o}
    function render(){
      document.querySelectorAll('.mode button').forEach(b=>b.classList.toggle('on',b.dataset.m===mode));
      $('grades').hidden=mode!=='class';$('tpick').hidden=mode!=='teacher';$('fhint').hidden=mode!=='free';$('pickh').textContent=mode==='class'?X.pick:mode==='teacher'?X.pickt:X.fp_h;
      const isF=mode==='free';$('freebox').hidden=!isF;$('ttprint').hidden=true;document.querySelector('.ttmain .seg').hidden=isF;
      if(isF){const main=document.querySelector('.ttmain');main.classList.remove('empty');view='day';$('quick').hidden=false;$('lessons').hidden=true;$('week').hidden=true;
        document.querySelectorAll('#quick button').forEach(b=>b.classList.toggle('on',+b.dataset.d===day&&((b.dataset.q==='today'&&day===today)||(b.dataset.q==='tom'&&day===tomorrow))));
        $('dtabs').hidden=false;$('dtabs').innerHTML=K.map((k,n)=>`<button type="button" role="tab" aria-selected="${n===day}" data-d="${n}"><b>${X.short[n]}</b><small>${n===today?X.today:n===tomorrow?X.tom:''}</small></button>`).join('');
        renderFree();tick();return}
      document.querySelectorAll('.cl').forEach(b=>b.classList.toggle('on',mode==='class'&&b.dataset.c===cls));
      $('tsel').value=tch||'';
      const main=document.querySelector('.ttmain'),cur=sel();main.classList.toggle('empty',!cur);
      if(!cur){$('ttcls').textContent=mode==='class'?X.pick:X.pickt;$('ttcount').textContent='';$('dtabs').innerHTML='';$('lessons').innerHTML='';$('week').hidden=true;$('quick').hidden=true;tick();return}
      if(mode==='class'){const h=(D.hd||{})[cls];$('ttcls').innerHTML=esc(cls+' '+X.cls)+(h?`<span class="tthd">${esc(X.ht)}: <b>${esc(h)}</b></span>`:'')}else $('ttcls').textContent=tch;
      $('quick').hidden=view!=='day';
      document.querySelectorAll('#quick button').forEach(b=>b.classList.toggle('on',+b.dataset.d===day&&((b.dataset.q==='today'&&day===today)||(b.dataset.q==='tom'&&day===tomorrow))));
      $('dtabs').innerHTML=K.map((k,n)=>{const c=Object.keys(les(n)).length;return `<button type="button" role="tab" aria-selected="${n===day}" data-d="${n}"><b>${X.short[n]}</b><small>${n===today?X.today:n===tomorrow?X.tom:X.count.replace('{n}',c)}</small></button>`}).join('');
      $('dtabs').hidden=view!=='day';
      const ls=les(day),ps=Object.keys(ls).map(Number),max=ps.length?Math.max(...ps):0,min=ps.length?Math.min(...ps):1;
      $('ttcount').textContent=view==='day'?X.days[day]+' · '+X.count.replace('{n}',ps.length):(mode==='teacher'?subj(TS[tch])[0]:'');
      let out='';
      if(!ps.length)out=`<li class="free"><span class="pn">–</span><div><b>${X.nol}</b></div></li>`;
      for(let p=min;p<=max&&ps.length;p++){const c=ls[p],tm=B[p-1]?B[p-1][0]+' – '+B[p-1][1]:'';
        if(!c){out+=`<li class="free" data-p="${p}"><span class="pn">${p}</span><div><b>${X.free}</b><small>${tm}</small></div></li>`;continue}
        out+=`<li style="--sc:${c.col}" data-p="${p}"><span class="pn">${p}</span><div><span class="tm">${tm}</span><b>${esc(c.name)}</b><small>${esc(c.sub)}</small></div><span class="si"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${IC[c.col]||''}</svg></span></li>`}
      $('lessons').innerHTML=out;$('lessons').hidden=view!=='day';
      if(view==='week'){const W=K.map((k,n)=>les(n));let mp=0;W.forEach(o=>Object.keys(o).forEach(p=>mp=Math.max(mp,+p)));
        let tb='<table class="wk"><thead><tr><th>#</th>'+K.map((k,n)=>`<th${n===today?' class="td"':''}>${X.short[n]}</th>`).join('')+'</tr></thead><tbody>';
        for(let p=1;p<=mp;p++){tb+=`<tr><th>${p}<small>${B[p-1]?B[p-1][0]:''}</small></th>`+W.map((o,n)=>{const c=o[p],cl=n===today?' class="td"':'';if(!c)return `<td${cl}></td>`;return `<td${cl}><span style="--sc:${c.col}">${esc(mode==='teacher'?c.name.split(' ')[0]:c.name)}</span></td>`}).join('')+'</tr>'}
        $('week').innerHTML=tb+'</tbody></table>'}
      $('week').hidden=view!=='week';
      pdfLink();tick();
    }
    function tick(){
      const n=now(),cur=n.h*60+n.m+n.s/60;$('clk').textContent=String(n.h).padStart(2,'0')+':'+String(n.m).padStart(2,'0');
      let msg='',pct=0,live=0;const d=n.wd<=4?n.wd:-1;
      const L=mode!=='free'&&sel()&&d>=0?les(d):null,ps0=L?Object.keys(L).map(Number):null;
      if(d<0)msg=X.off;else{const ps=B.map((b,k)=>k+1).filter(p=>!ps0||ps0.includes(p));
        if(!ps.length)msg=X.off;
        else if(cur<mm(B[ps[0]-1][0]))msg=X.before.replace('{t}',B[ps[0]-1][0]);
        else if(cur>=mm(B[ps[ps.length-1]-1][1]))msg=X.done;
        else for(const p of ps){const a=mm(B[p-1][0]),e=mm(B[p-1][1]);
          if(cur>=a&&cur<e){live=p;pct=(cur-a)/(e-a)*100;const nm=L&&L[p]?L[p].name+' · ':'';msg=`<b>${X.now}: ${X.lno.replace('{p}',p)}</b> · ${esc(nm)}${X.ends.replace('{m}',Math.ceil(e-cur))}`;break}
          if(cur<a){const nx=L&&L[p]?' · '+esc(L[p].name):'';msg=`<b>${X.brk}</b> · ${X.next.replace('{t}',B[p-1][0])}${nx}`;break}}}
      $('status').innerHTML=msg;$('barfill').style.width=pct+'%';document.querySelector('.ttclock').classList.toggle('live',!!live);
      document.querySelectorAll('#lessons li').forEach(li=>li.classList.toggle('cur',!!live&&day===d&&+li.dataset.p===live));
      document.querySelectorAll('.btab tr').forEach(r=>r.classList.toggle('cur',!!live&&+r.dataset.p===live));
    }
    setInterval(tick,15000);
    const save=()=>{try{localStorage.setItem('ttmode',mode);cls&&localStorage.setItem('ttcls',cls);tch&&localStorage.setItem('tttch',tch)}catch(e){}
      history.replaceState(null,'','#'+(mode==='free'?'free':mode==='class'?(cls||'').toLowerCase():(tch?slug(tch):'')))};
    const jump=()=>{if(innerWidth<900)document.querySelector('.ttmain').scrollIntoView({block:'start'})};
    $('grades').addEventListener('click',e=>{const b=e.target.closest('.cl');if(!b)return;cls=b.dataset.c;save();render();jump()});
    $('tsel').addEventListener('change',()=>{tch=$('tsel').value||null;save();render();if(tch)jump()});
    document.querySelectorAll('.mode button').forEach(b=>b.addEventListener('click',()=>{mode=b.dataset.m;save();render()}));
    $('dtabs').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;day=+b.dataset.d;render()});
    $('quick').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;day=+b.dataset.d;view='day';document.querySelectorAll('.ttmain .seg button').forEach(x=>x.classList.toggle('on',x.dataset.v==='day'));render()});
    document.querySelectorAll('.ttmain .seg button').forEach(b=>b.addEventListener('click',()=>{view=b.dataset.v;document.querySelectorAll('.ttmain .seg button').forEach(x=>x.classList.toggle('on',x===b));render()}));
    const pdfBase=document.querySelector('.ttwrap').dataset.pdf;
    function pdfLink(){const a=$('ttprint'),cur=sel();a.hidden=mode==='free'||!cur;if(a.hidden)return;
      const f=mode==='class'?'c-'+cls.toLowerCase():slug(tch);a.href=pdfBase+f+'.pdf';a.setAttribute('download',(mode==='class'?cls:tch).replace(/\s+/g,'_')+'.pdf')}
    let dp=null;addEventListener('beforeinstallprompt',e=>{e.preventDefault();dp=e;$('ttinst').hidden=false});
    $('ttinst').addEventListener('click',async()=>{if(!dp)return;dp.prompt();try{await dp.userChoice}catch(e){};dp=null;$('ttinst').hidden=true});
    if(/iphone|ipad|ipod/i.test(navigator.userAgent)&&!navigator.standalone)$('ttios').hidden=false;
    $('fper').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;
      if(b.dataset.p==='all'){if(fsel.size===B.length)fsel.clear();else B.forEach((x,k)=>fsel.add(k+1))}else{const p=+b.dataset.p;fsel.has(p)?fsel.delete(p):fsel.add(p)}render()});
    $('fsub').addEventListener('change',()=>{fsub=$('fsub').value;render()});
    render();
  }

  const lb=document.getElementById('lbdata');
  if(lb){
    const L=JSON.parse(lb.textContent),X=L.t,B=L.b,K=['mon','tue','wed','thu','fri'],bar=document.getElementById('livebar'),tx=document.getElementById('lbtxt');
    const mm=s=>{const[h,m]=s.split(':');return +h*60+ +m};
    const esc=s=>String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
    let mode='class',cls=null,tch=null;try{mode=localStorage.getItem('ttmode')||'class';cls=localStorage.getItem('ttcls');tch=localStorage.getItem('tttch')}catch(e){}
    const who=mode==='teacher'?tch:cls;
    if(!who){tx.textContent=X.choose;bar.hidden=false}
    else fetch(document.querySelector('link[rel=icon][href$="logo.png"]').href.replace(/logo\.png$/,'timetable.json')).then(r=>r.json()).then(D=>{
      const C=D.classes;
      function les(k){const o={};if(mode==='class'&&C[cls]){const T=C[cls][k]||{};for(const p in T)o[p]=(L.s[T[p][0][0]]||[T[p][0][0]])[0]}
        else{for(const c in C){const T=C[c][k]||{};for(const p in T)if(T[p].some(x=>x[1]===tch))o[p]=c+' '+X.cls}}return o}
      function tick(){const p={};new Intl.DateTimeFormat('en-US',{timeZone:'Asia/Samarkand',weekday:'long',hour:'2-digit',minute:'2-digit',hourCycle:'h23'}).formatToParts(new Date()).forEach(x=>p[x.type]=x.value);
        const wd=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(String(p.weekday).slice(0,3)),cur=+p.hour*60+ +p.minute;let msg='';
        if(wd>4)msg=X.off;else{const O=les(K[wd]),ps=Object.keys(O).map(Number).sort((a,b)=>a-b);
          if(!ps.length)msg=X.off;else if(cur<mm(B[ps[0]-1][0]))msg=X.before.replace('{t}',B[ps[0]-1][0]);else if(cur>=mm(B[ps[ps.length-1]-1][1]))msg=X.done;
          else for(const q of ps){const a=mm(B[q-1][0]),e=mm(B[q-1][1]);if(cur>=a&&cur<e){msg=`<b>${X.now}: ${X.lno.replace('{p}',q)}</b> · ${esc(O[q])} · ${X.ends.replace('{m}',e-cur)}`;break}
            if(cur<a){msg=`<b>${X.brk}</b> · ${X.next.replace('{t}',B[q-1][0])} · ${esc(O[q])}`;break}}}
        tx.innerHTML=`<strong>${esc(who)}</strong> · ${msg}`;bar.hidden=false}
      tick();setInterval(tick,30000)}).catch(()=>{});
  }
  const yc=document.querySelectorAll('.ychips .chip');
  yc.forEach(b=>b.addEventListener('click',()=>{yc.forEach(x=>x.classList.toggle('on',x===b));document.querySelectorAll('.gview').forEach(v=>v.hidden=v.dataset.y!==b.dataset.y)}));
  const pcs=document.querySelectorAll('.pchips .pc');
  pcs.forEach(b=>b.addEventListener('click',()=>{pcs.forEach(x=>x.classList.toggle('on',x===b));document.querySelectorAll('.ppanel').forEach(p=>p.hidden=p.dataset.f!==b.dataset.f)}));
  const gq=document.getElementById('gq');
  if(gq){let gy=document.querySelector('.gyears .chip.on').dataset.y,gk='all';const rows=[...document.querySelectorAll('#glist tbody tr')],kc=document.querySelectorAll('.gkinds .chip');
    const run=()=>{const v=gq.value.trim().toLowerCase();let n=0;const cnt={all:0,uni:0,col:0,none:0};
      rows.forEach(r=>{const iy=v||gy==='all'||r.dataset.y===gy,iq=!v||r.dataset.q.includes(v);if(iy&&iq){cnt.all++;cnt[r.dataset.k]++}const ok=iy&&iq&&(gk==='all'||r.dataset.k===gk);r.hidden=!ok;if(ok)n++});
      kc.forEach(b=>{b.querySelector('em').textContent=cnt[b.dataset.k];b.hidden=b.dataset.k!=='all'&&!cnt[b.dataset.k]&&gk!==b.dataset.k});document.getElementById('gnone').hidden=n>0};
    document.querySelectorAll('.gyears .chip').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.gyears .chip').forEach(x=>x.classList.toggle('on',x===b));gy=b.dataset.y;gq.value='';run()}));
    kc.forEach(b=>b.addEventListener('click',()=>{kc.forEach(x=>x.classList.toggle('on',x===b));gk=b.dataset.k;run()}));
    gq.addEventListener('input',run);run()}
  if('serviceWorker' in navigator){const ic=document.querySelector('link[rel=icon][href$="logo.png"]');navigator.serviceWorker.register(ic.href.replace(/logo\.png$/,'sw.js')).catch(()=>{})}
  const bd=document.getElementById('belldata');
  if(bd){const D=JSON.parse(bd.textContent),T=D.t,B=D.b,$=id=>document.getElementById(id),C=+$('bell').dataset.c;
    const mm=s=>{const[h,m]=s.split(':');return(+h*60+ +m)*60},pad=n=>String(n).padStart(2,'0');
    const fmt=s=>{s=Math.max(0,Math.round(s));if(s>=86400){const d=Math.floor(s/86400),r=s%86400;return`${d} ${T.dunit} ${Math.floor(r/3600)}:${pad(Math.floor(r%3600/60))}`}const h=Math.floor(s/3600),m=Math.floor(s%3600/60),x=s%60;return h?`${h}:${pad(m)}:${pad(x)}`:`${pad(m)}:${pad(x)}`};
    const esc=s=>String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
    let cls=null,ALL=null;const rc=()=>{try{return(localStorage.getItem('ttmode')||'class')==='class'?localStorage.getItem('ttcls'):null}catch(e){return null}};
    fetch(document.querySelector('link[rel=icon][href$="logo.png"]').href.replace(/logo\.png$/,'timetable.json')).then(r=>r.json()).then(j=>{ALL=j.classes;tick()}).catch(()=>{});
    const K=['mon','tue','wed','thu','fri'];
    const subj=(wd,p)=>{const TT=ALL&&cls?ALL[cls]:null;if(!TT||wd>4)return null;const d=TT[K[wd]]||{},x=d[p];if(!x)return null;const k=x[0][0];return(D.s[k]||[k])[0]};
    const lis=[...document.querySelectorAll('#bline li')];
    function now(){const p={};new Intl.DateTimeFormat('en-US',{timeZone:'Asia/Samarkand',weekday:'short',hour:'2-digit',minute:'2-digit',second:'2-digit',hourCycle:'h23'}).formatToParts(new Date()).forEach(x=>p[x.type]=x.value);
      return{wd:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(p.weekday),s:+p.hour*3600+ +p.minute*60+ +p.second,h:p.hour,m:p.minute}}
    function nextDay(wd){let d=1;while((wd+d)%7>4)d++;return d}
    function tick(){cls=rc();$('bchoose').hidden=!!cls;const N=now(),wd=N.wd,s=N.s,first=mm(B[0][0]),last=mm(B[B.length-1][1]);
      $('bclock').textContent=`${T.days[wd]}, ${N.h}:${N.m}`;
      let state='',left=0,total=1,until='',next='',cur=0,gap=0,done=0,mode='';
      if(wd>4||s>=last){const d=wd>4?nextDay(wd):nextDay(wd);left=d*86400-s+first;total=left;mode='off';
        state=wd>4?T.weekend:T.done;until=T.before;next=T.next.replace('{d}',d===1&&wd<=4?T.tom:T.days[(wd+d)%7]).replace('{t}',B[0][0]);done=wd>4?0:B.length}
      else if(s<first){left=first-s;total=Math.max(left,3600);state=T.before;until=T.starts.replace('{t}',B[0][0]);mode='pre'}
      else{for(let k=0;k<B.length;k++){const a=mm(B[k][0]),e=mm(B[k][1]);
          if(s>=a&&s<e){cur=k+1;left=e-s;total=e-a;state=T.lesson.replace('{p}',cur);until=T.until.replace('{t}',B[k][1]);done=k;mode='les';
            next=k+1<B.length?T.nextl.replace('{l}',T.lesson.replace('{p}',k+2)).replace('{t}',B[k+1][0]):T.lastl;break}
          if(k+1<B.length&&s>=e&&s<mm(B[k+1][0])){gap=k+1;const n=mm(B[k+1][0]);left=n-s;total=n-e;state=(total>=1200?T.lunch:T.brk);until=T.until.replace('{t}',B[k+1][0]);done=k+1;mode='brk';
            next=T.nextl.replace('{l}',T.lesson.replace('{p}',k+2)).replace('{t}',B[k+1][0]);break}}}
      const bell=$('bell');bell.dataset.m=mode;
      $('bstate').textContent=state;$('bcount').textContent=fmt(left);$('buntil').textContent=until;$('bnext').textContent=next;
      const f=mode==='off'?0:Math.min(1,Math.max(0,1-left/total));$('barc').setAttribute('stroke-dasharray',`${(C*f).toFixed(1)} ${C}`);$('barc').style.opacity=f>0?1:0;
      $('bprogt').textContent=T.prog.replace('{a}',done).replace('{n}',B.length);$('bprogb').style.width=(done/B.length*100)+'%';
      const sp=mode==='les'?cur:mode==='brk'?gap+1:mode==='pre'?1:0,sj=sp?subj(wd,sp):null;
      $('bsubj').innerHTML=cls?(`<b>${esc(cls)} ${esc(T.cls)}</b>`+(sj&&mode==='les'?` · ${esc(sj)}`:'')):'';if(sj&&mode!=='les')$('bnext').textContent=(mode==='pre'?T.nextl.replace('{l}',T.lesson.replace('{p}',1)).replace('{t}',B[0][0]):next)+' · '+sj;$('bsubj').hidden=!cls;
      const wk=wd<=4;lis.forEach(li=>{const p=+li.dataset.p||0,g=+li.dataset.g||0,end=p?mm(B[p-1][1]):mm(B[g][0]);
        li.classList.toggle('past',wk&&s>=end);li.classList.toggle('now',(mode==='les'&&p===cur)||(mode==='brk'&&g===gap))})}
    tick();setInterval(tick,1000)}
  const f=document.getElementById('f'),ok=document.getElementById('ok');
  if(f)f.addEventListener('submit',async e=>{
    e.preventDefault();
    if(f.botcheck&&f.botcheck.checked)return;
    if(!f.n.value.trim()||!f.m.value.trim()){ok.textContent="Пожалуйста, укажите имя и сообщение.";return}
    const FX=["Отправка…", "Спасибо! Сообщение отправлено. Мы скоро свяжемся с вами.", "Не удалось отправить. Позвоните или напишите в Telegram.", "Открылось приложение почты. Отправьте сообщение оттуда или свяжитесь по телефону / в Telegram."],KEY="a9aa2bb5-5bc2-4b33-a802-1eab51f19597",btn=f.querySelector('button');
    if(!KEY){
      const body=f.m.value.trim()+'\n\n'+f.n.value.trim()+(f.ph.value.trim()?'\n'+f.ph.value.trim():'');
      ok.textContent=FX[3];
      location.href='mailto:ixm013@piima.uz?subject='+encodeURIComponent('kegeyliqm.uz — '+f.n.value.trim())+'&body='+encodeURIComponent(body);
      return}
    btn.disabled=true;ok.textContent=FX[0];
    try{
      const r=await fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({access_key:KEY,subject:'kegeyliqm.uz — '+f.n.value.trim(),from_name:'kegeyliqm.uz',name:f.n.value.trim(),phone:f.ph.value.trim(),message:f.m.value.trim(),botcheck:''})});
      const j=await r.json();
      if(j.success){ok.textContent=FX[1];f.reset()}else{ok.textContent=FX[2]}
    }catch(x){ok.textContent=FX[2]}
    btn.disabled=false;
  });
}

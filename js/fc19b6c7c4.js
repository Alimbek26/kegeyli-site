(function(){
var D=PLD,U=D.ui,$=function(i){return document.getElementById(i)},KEY='abroadPlan';
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]})};
var IC=function(p,s){return '<svg viewBox="0 0 24 24" width="'+(s||20)+'" height="'+(s||20)+'" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+p+'</svg>'};
var P={a:{},done:{},step:0,built:false};
try{var raw=localStorage.getItem(KEY);if(raw){var o=JSON.parse(raw);if(o&&o.a)P=Object.assign(P,o)}}catch(e){}
function save(){try{localStorage.setItem(KEY,JSON.stringify(P))}catch(e){}}
var CS={};D.cs.forEach(function(c){CS[c.k]=c});
var now=new Date(),T0=new Date(now.getFullYear(),now.getMonth(),now.getDate());
function pd(s){var p=s.split('-');return new Date(+p[0],+p[1]-1,+(p[2]||1))}
function ds(d){return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
function addD(d,n){var x=new Date(d);x.setDate(x.getDate()+n);return x}
function mn(d){var m=(D.mong||D.mon)[d.getMonth()];return D.lang===1?m:m.toLowerCase()}
function fd(d){return d.getDate()+' '+mn(d)+' '+d.getFullYear()}
function fmtUSD(v){return '$'+Math.round(v).toLocaleString('en-US')}
function rep(s,o){for(var k in o)s=s.split('{'+k+'}').join(o[k]);return s}
/* ---------- wizard ---------- */
var STEPS=[
 {k:'g',q:U.q_grade,h:U.h_grade,o:[9,10,11,12].map(function(n){return {v:n,l:n===12?U.g12:rep(U.g,{n:n}),big:n===12?'✓':String(n)}})},
 {k:'c',q:U.q_c,h:U.h_c,multi:3,o:D.cs.map(function(c){return {v:c.k,l:c.n,flag:c.f}})},
 {k:'f',q:U.q_f,h:U.h_f,o:['eng','med','bus','sci','hum','und'].map(function(k){return {v:k,l:U['f_'+k],ic:D.fi[k]}})},
 {k:'m',q:U.q_a,h:U.h_a,o:['top','strong','value'].map(function(k){return {v:k,l:U['a_'+k],s:U['a_'+k+'_s'],ic:D.ai[k]}})},
 {k:'i',q:U.q_i,h:U.h_i,o:[{v:0,l:U.i0,big:'—'},{v:4.5,l:U.i45,big:'<5'},{v:5,big:'5.0'},{v:5.5,big:'5.5'},{v:6,big:'6.0'},{v:6.5,big:'6.5'},{v:7,big:'7.0'},{v:7.5,big:'7.5+'}]},
 {k:'s',q:U.q_s,h:U.h_s,o:[{v:0,l:U.s0,big:'—'},{v:950,l:U.s950,big:'<1000'},{v:1100,big:'1000–1190'},{v:1270,big:'1200–1340'},{v:1400,big:'1350–1440'},{v:1480,big:'1450+'}]},
 {k:'b',q:U.q_b,h:U.h_b,o:D.bud.map(function(b){return {v:b.v,big:b.big,l:b.l}})},
 {k:'x',q:U.q_x,h:U.h_x,o:[{v:'full',l:U.x_full,big:'★'},{v:'part',l:U.x_part,big:'½'},{v:'none',l:U.x_none,big:'✓'}]}
];
function answered(st){var v=P.a[st.k];return st.multi?(v&&v.length>0):v!==undefined}
function wiz(){
 var st=STEPS[P.step],n=STEPS.length,w=$('plwiz');
 var opts=st.o.map(function(o){var v=P.a[st.k],on=st.multi?(v||[]).indexOf(o.v)>=0:v===o.v;
  return '<button type="button" class="plopt'+(on?' on':'')+(o.flag?' flag':'')+(o.ic?' ic':'')+'" data-v="'+esc(o.v)+'" aria-pressed="'+on+'">'
   +(o.flag?'<span class="plf">'+o.flag+'</span>':o.ic?'<span class="pli">'+IC(o.ic,22)+'</span>':o.big?'<span class="plbig">'+esc(o.big)+'</span>':'')
   +(o.l?'<span class="pll">'+esc(o.l)+'</span>':'')+(o.s?'<small>'+esc(o.s)+'</small>':'')+(on?'<span class="plck">'+IC('<path d="M5 12l5 5L20 7"/>',14)+'</span>':'')+'</button>'}).join('');
 var cnt=st.multi?'<span class="plcnt">'+((P.a[st.k]||[]).length)+' / '+st.multi+'</span>':'';
 w.innerHTML='<div class="plprog"><span style="width:'+Math.round((P.step+1)/n*100)+'%"></span></div>'
  +'<div class="plstep">'+rep(U.step,{n:P.step+1,t:n})+cnt+'</div><h3 class="plq">'+esc(st.q)+'</h3><p class="plh">'+esc(st.h)+'</p>'
  +'<div class="plopts c'+st.k+'">'+opts+'</div><div class="plnav">'
  +(P.step>0?'<button type="button" class="btn s" id="plback">← '+esc(U.back)+'</button>':'<span></span>')
  +'<button type="button" class="btn p" id="plnext"'+(answered(st)?'':' disabled')+'>'+esc(P.step===n-1?U.build:U.next)+(P.step===n-1?' ✓':' →')+'</button></div>';
 [].forEach.call(w.querySelectorAll('.plopt'),function(b){b.onclick=function(){
   var raw=b.dataset.v,o=st.o.filter(function(x){return String(x.v)===raw})[0],v=o.v;
   if(st.multi){var a=(P.a[st.k]||[]).slice(),ix=a.indexOf(v);if(ix>=0)a.splice(ix,1);else{if(a.length>=st.multi)a.shift();a.push(v)}P.a[st.k]=a;save();wiz()}
   else{P.a[st.k]=v;save();wiz();setTimeout(function(){if(P.step<n-1){P.step++;save();wiz();top()}},180)}}});
 if($('plback'))$('plback').onclick=function(){P.step--;save();wiz();top()};
 $('plnext').onclick=function(){if(!answered(st))return;if(P.step<n-1){P.step++;save();wiz();top()}else{P.built=true;save();show()}};
}
function top(){var e=$('pl');if(e&&e.getBoundingClientRect().top<0)e.scrollIntoView({behavior:'smooth'})}
/* ---------- plan logic ---------- */
function calc(){
 var a=P.a,sel=(a.c||[]).map(function(k){return CS[k]}).filter(Boolean),amb=a.m,g=a.g;
 var sY=now.getMonth()>=8?now.getFullYear():now.getFullYear()-1,A=g===12?sY:sY+(11-g),start=A+1;
 var adj=amb==='top'?0.5:amb==='value'?-0.5:0;
 var ieT=0;sel.forEach(function(c){ieT=Math.max(ieT,Math.max(5.5,c.ie+adj))});
 var satNeed=sel.some(function(c){return c.sat===2})?2:sel.some(function(c){return c.sat===1})?1:0;
 var satT=amb==='top'?1450:amb==='strong'?1300:1150;
 var bud=a.b,x=a.x;
 /* countries */
 var fits=sel.map(function(c){
  var R=[],pts=0,money=a.b>=c.ty?2:a.b>=c.lo?1:0;
  if(x==='full'){if(c.sch==='gov'){pts+=3;R.push(['ok',U.s_gov])}else if(c.sch==='need'){pts+=1;R.push(['warn',U.s_need])}else{R.push(['no',U.s_none])}}
  else{if(money===2){pts+=3;R.push(['ok',U.m_ok])}else if(money===1){pts+=2;R.push(['warn',U.m_lo])}else if(c.sch==='gov'){pts+=2;R.push(['warn',U.m_no+' · '+U.s_gov])}else if(c.sch==='need'){pts+=1;R.push(['warn',U.m_no+' · '+U.s_need])}else R.push(['no',U.m_no])}
  var t=Math.max(5.5,c.ie+adj),gp=Math.round((t-(a.i||0))*10)/10,young=g<=10;
  if(!a.i){pts+=young?1:0;R.push(['warn',rep(U.e_none,{t:t.toFixed(1)})])}else if(gp<=0){pts+=2;R.push(['ok',rep(U.e_ok,{t:t.toFixed(1)})])}else{pts+=gp<=1||young?1:0;R.push([gp<=1?'warn':'no',rep(U.e_gap,{t:t.toFixed(1),g:gp.toFixed(1)})])}
  if(c.sat){if(a.s>=satT){pts+=2;R.push(['ok',U.t_ok])}else{pts+=(a.s>=satT-150||young)?1:0;R.push([c.sat===2?'warn':'info',rep(U.t_gap,{t:satT})])}}else{pts+=2;R.push(['ok',U.t_no])}
  if(c.loc)R.push(['info',U.loc]);
  return {c:c,fit:pts>=6?2:pts>=4?1:0,R:R,money:money}});
 /* timeline */
 var ev=[],shift=A-2026,usuk=sel.some(function(c){return ['usa','uk','singapore'].indexOf(c.k)>=0}),ks=sel.map(function(c){return c.k});
 function E(id,d,cat,t,n,u,exp,flag){ev.push({id:id,d:d,cat:cat,t:t,n:n||'',u:u||'',exp:!!exp,f:flag||''})}
 function at(m,d,y){return new Date(y==null?A:y,m-1,d)}
 function fut(d,fallback){return d<T0?addD(T0,fallback):d}
 D.ev.forEach(function(e,n){if(ks.indexOf(e.k)<0)return;var d=pd(e.d);d.setFullYear(d.getFullYear()+shift);E('dl'+n,d,'dl',e.t,e.n,e.u,e.e||shift>0,CS[e.k].f)});
 ['canada','germany','korea','malaysia'].forEach(function(k){if(ks.indexOf(k)>=0)E('op'+k,fut(at(10,1),21),'dl',rep(U.e_open,{c:CS[k].n}),'',CS[k].u,true,CS[k].f)});
 var ieBy=usuk?at(9,30):at(10,31),prepW=!a.i?24:Math.max(4,Math.min(24,Math.round((ieT-a.i)*16)));
 if(a.i<ieT){var ps=addD(ieBy,-prepW*7);E('iprep',ps<T0?T0:ps,'exam',rep(U.e_iprep,{t:ieT.toFixed(1)}),rep(U.x_prep,{w:prepW}),D.L.ielts);
  if(ieBy<addD(T0,42))E('itake',addD(T0,Math.max(42,prepW*7)),'exam',U.e_iasap,U.x_ielts_note,D.L.ielts);else E('itake',ieBy,'exam',U.e_itake,U.x_ielts_note,D.L.ielts)}
 var satList=[];
 if(satNeed&&a.s<satT){E('spr',addD(T0,14),'exam',U.e_spr,'',D.L.sat);
  D.sat.forEach(function(s){var d=pd(s.d);if(d>T0&&(!s.r||addD(pd(s.r),4)>=T0)&&d<=at(12,31)&&satList.length<2){satList.push(s);E('sat'+s.d,d,'exam',U.e_sat,s.r?rep(U.x_reg,{d:fd(pd(s.r))}):'',D.L.sat)}});
  if(!satList.length)E('satg',fut(at(3,1),30),'exam',U.e_satg,'',D.L.sat)}
 if(g<=10)E('act',at(6,15),'school',U.e_act,U.e_actn);
 E('pass',fut(at(6,1),14),'doc',U.e_pass,'',D.L.ck);
 if(usuk||ks.indexOf('canada')>=0)E('essay',fut(at(6,1),7),'app',U.e_essay,'',D.L.essay);
 if(usuk||ks.indexOf('canada')>=0)E('rec',fut(at(9,15),10),'doc',U.e_rec,'',D.L.ck);
 E('tr',fut(at(9,1),14),'doc',U.e_tr,'',D.L.ck);
 if(ks.indexOf('usa')>=0)E('aid',fut(at(11,1),14),'money',U.e_aid,U.e_aidn,D.L.sch);
 if(ks.indexOf('usa')>=0)E('usdec',at(3,31,start),'app',U.e_usdec,'',D.L.app);
 if(ks.indexOf('uk')>=0)E('ukdec',at(5,15,start),'app',U.e_ukdec,'',D.L.app);
 E('visa',at(5,15,start),'visa',U.e_visa,U.e_visan,D.L.ck);
 E('fly',at(8,20,start),'go',U.e_fly,(ks.indexOf('korea')>=0||ks.indexOf('japan')>=0)?U.e_flyn:'');
 ev.sort(function(p,q){return p.d-q.d});
 var firstDl=ev.filter(function(e){return e.cat==='dl'&&e.d>=T0&&e.id.indexOf('op')!==0})[0],passedDl=ev.some(function(e){return e.cat==='dl'&&e.d<T0});
 /* readiness */
 var sE=!a.i?(g<=10?8:3):a.i>=ieT?25:ieT-a.i<=0.5?17:ieT-a.i<=1?10:5;
 var sT=!satNeed?25:a.s>=satT?25:a.s>=satT-150?16:a.s?9:(g<=10?9:4);
 var cheap=Math.min.apply(null,sel.map(function(c){return c.lo})),hasGov=sel.some(function(c){return c.sch==='gov'}),hasNeed=sel.some(function(c){return c.sch==='need'});
 var sM=x==='full'?(hasGov?18:hasNeed?10:4):bud>=Math.min.apply(null,sel.map(function(c){return c.ty}))?25:bud>=cheap?19:hasGov?14:hasNeed?8:4;
 var mo=firstDl?(firstDl.d-T0)/864e5/30:(at(12,1)-T0)/864e5/30,sTi=mo>18?25:mo>9?21:mo>4?14:mo>1.5?9:5;
 var score=sE+sT+sM+sTi;
 return {sel:sel,fits:fits,ev:ev,A:A,start:start,ieT:ieT,satNeed:satNeed,satT:satT,satList:satList,prepW:prepW,ieBy:ieBy,score:score,parts:[[U.k_eng,sE],[U.k_test,sT],[U.k_money,sM],[U.k_time,sTi]],firstDl:firstDl,passedDl:passedDl,hasGov:hasGov,hasNeed:hasNeed};
}
var CAT={dl:['#a3202c','<path d="M12 8v4l3 2"/><circle cx="12" cy="12" r="9"/>'],exam:['#7c3aed','<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>'],doc:['#0b7a8f','<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>'],
 app:['#2a7fd1','<path d="M4 20h4L18.500 9.500a2.800 2.800 0 0 0-4-4L4 16v4z"/>'],money:['#d97706','<circle cx="12" cy="12" r="9"/><path d="M14.500 9.500c-.5-1-1.500-1.500-2.500-1.500-1.400 0-2.500.8-2.500 2s1.100 1.700 2.500 2 2.500.8 2.500 2-1.100 2-2.500 2c-1 0-2-.5-2.500-1.500M12 6.500v11"/>'],
 visa:['#15803d','<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="12" r="2.500"/><path d="M14 10h4M14 14h3"/>'],school:['#be185d','<path d="M12 2.500l2.600 5.300 5.900.9-4.300 4.100 1 5.800L12 15.900l-5.200 2.700 1-5.800L3.500 8.700l5.900-.9z"/>'],
 go:['#0b5f78','<path d="M2 16l20-8-8 14-2-6z"/>']};
function show(){
 var R=calc(),a=P.a,w=$('plwiz'),r=$('plres');w.hidden=true;r.hidden=false;
 var sc=R.score,lv=sc>=80?3:sc>=60?2:sc>=40?1:0,C=2*Math.PI*52;
 var gl=a.g===12?U.g12:rep(U.g,{n:a.g});
 var hero='<section class="plhero"><div class="plht"><small>'+esc(U.r_for)+'</small><h3>'+R.sel.map(function(c){return c.f}).join(' ')+' '+esc(R.sel.map(function(c){return c.n}).join(' · '))+'</h3>'
  +'<div class="plchips"><span>'+esc(gl)+'</span><span>'+IC(D.fi[a.f],14)+esc(U['f_'+a.f])+'</span><span>'+esc(U.r_start)+': '+esc(D.mon[8])+' '+R.start+'</span></div>'
  +'<div class="plparts">'+R.parts.map(function(p){return '<div><span>'+esc(p[0])+'</span><i><b style="width:'+(p[1]*4)+'%"></b></i></div>'}).join('')+'</div></div>'
  +'<div class="plring"><svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="52" class="rb"/><circle cx="60" cy="60" r="52" class="rf l'+lv+'" style="stroke-dasharray:'+C+';stroke-dashoffset:'+(C*(1-sc/100))+'" transform="rotate(-90 60 60)"/></svg><div><b>'+sc+'</b><small>'+esc(U.ready)+'</small><em class="l'+lv+'">'+esc(U['rl'+lv])+'</em></div></div></section>';
 var notes='';if(a.g===12)notes+='<p class="plnote">'+esc(U.gap)+'</p>';if(R.passedDl&&(a.g>=11))notes+='<p class="plnote warn">'+esc(U.late)+'</p>';
 /* actions */
 var acts=[];
 if(R.firstDl&&(R.firstDl.d-T0)/864e5<=75)acts.push(['dl',rep(U.a_dl,{t:R.firstDl.t,d:fd(R.firstDl.d)}),R.firstDl.u]);
 if(!a.i)acts.push(['exam',U.a_i0,D.L.ielts]);else if(a.i<R.ieT)acts.push(['exam',rep(U.a_ig,{g:(R.ieT-a.i).toFixed(1)}),D.L.ielts]);
 if(R.satNeed&&!a.s)acts.push(['exam',U.a_s0,D.L.sat]);else if(R.satNeed&&a.s<R.satT)acts.push(['exam',rep(U.a_sg,{t:R.satT}),D.L.sat]);
 if(a.x==='full'&&!R.hasGov)acts.push(['money',U.a_mo,D.L.sch]);
 if(acts.length<3&&R.sel.some(function(c){return ['usa','uk','canada','singapore'].indexOf(c.k)>=0}))acts.push(['app',U.a_es,D.L.essay]);
 acts=acts.slice(0,3);acts.push(['school',U.a_par,'']);
 var week='<section class="card plsec"><h3 class="plsh">'+IC('<path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/>')+esc(U.week_h)+'</h3><ol class="placts">'
  +acts.map(function(x){return '<li style="--cc:'+CAT[x[0]][0]+'"><span class="plai">'+IC(CAT[x[0]][1],18)+'</span>'+(x[2]?'<a href="'+esc(x[2])+'">'+esc(x[1])+' →</a>':'<span>'+esc(x[1])+'</span>')+'</li>'}).join('')+'</ol>'
  +'<div class="pltip"><b>'+IC(D.fi[a.f],16)+esc(U.f_tip)+'</b><p>'+esc(D.tips[a.f])+'</p></div></section>';
 /* countries */
 var cc='<section class="plsec"><h3 class="plsh">'+IC('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>')+esc(U.c_h)+'</h3><div class="plcgrid">'
  +R.fits.map(function(F){var c=F.c,rows='';for(var k in c.r)rows+='<dt>'+esc(U['r_'+k])+'</dt><dd>'+esc(c.r[k])+'</dd>';
   return '<article class="card plc f'+F.fit+'"><header><span class="plcf">'+c.f+'</span><div><h4>'+esc(c.n)+'</h4><span class="plfit">'+esc(U['fit'+F.fit])+'</span></div></header>'
   +'<div class="plcost"><small>'+esc(U.cost_y)+'</small><b>'+(c.lo===0&&c.ty===0?'$0':fmtUSD(c.lo)+' – '+fmtUSD(c.ty))+'</b></div>'
   +'<ul class="plr">'+F.R.map(function(x){return '<li class="'+x[0]+'">'+esc(x[1])+'</li>'}).join('')+'</ul>'
   +'<details><summary>'+esc(U.more)+'</summary><dl>'+rows+'</dl></details>'
   +'<div class="plcl"><a href="'+esc(D.L.co)+'">'+esc(U.cmp)+' →</a><a href="'+esc(c.u)+'" target="_blank" rel="noopener">'+esc(U.official)+' ↗</a></div></article>'}).join('')+'</div></section>';
 /* exams */
 var ieBox='<div class="plex"><h4>IELTS</h4><div class="plexn"><div><small>'+esc(U.x_now)+'</small><b>'+(a.i?a.i.toFixed(1):'—')+'</b></div><span class="plarr">→</span><div><small>'+esc(U.x_goal)+'</small><b>'+R.ieT.toFixed(1)+'</b></div></div>'
  +(a.i>=R.ieT?'<p class="ok">'+esc(U.x_done)+'</p>':'<p>'+esc(rep(U.x_prep,{w:R.prepW}))+'</p><p><b>'+esc(U.x_by)+':</b> '+esc(fd(R.ieBy<addD(T0,42)?addD(T0,Math.max(42,R.prepW*7)):R.ieBy))+'</p><p class="note">'+esc(U.x_ielts_note)+'</p>')
  +'<a class="btn s" href="'+esc(D.L.ielts)+'">IELTS →</a></div>';
 var satBox=R.satNeed?'<div class="plex"><h4>SAT</h4><div class="plexn"><div><small>'+esc(U.x_now)+'</small><b>'+(a.s?(a.s===950?'<1000':a.s===1480?'1450+':a.s):'—')+'</b></div><span class="plarr">→</span><div><small>'+esc(U.x_goal)+'</small><b>'+R.satT+'+</b></div></div>'
  +(a.s>=R.satT?'<p class="ok">'+esc(U.t_ok)+'</p>':R.satList.length?'<p><b>'+esc(U.x_sat_dates)+':</b></p><ul class="plsat">'+R.satList.map(function(s){return '<li><b>'+esc(fd(pd(s.d)))+'</b>'+(s.r?'<small>'+esc(rep(U.x_reg,{d:fd(pd(s.r))}))+'</small>':'<small>'+esc(U.exp)+'</small>')+'</li>'}).join('')+'</ul>':'<p>'+esc(U.e_satg)+'</p>')
  +'<a class="btn s" href="'+esc(D.L.sat)+'">SAT →</a></div>':'';
 var ex='<section class="card plsec"><h3 class="plsh">'+IC(CAT.exam[1])+esc(U.x_h)+'</h3><div class="plexg">'+ieBox+satBox+'</div></section>';
 /* timeline */
 var nx=R.ev.filter(function(e){return e.d>=T0&&!P.done[e.id]})[0],cur='',tl='',dn=R.ev.filter(function(e){return P.done[e.id]}).length;
 R.ev.forEach(function(e){var m=D.mon[e.d.getMonth()]+' '+e.d.getFullYear();if(m!==cur){tl+=(cur?'</ol>':'')+'<h4 class="plmo">'+esc(m)+'</h4><ol class="pltl">';cur=m}
  var past=e.d<T0,dd=Math.round((e.d-T0)/864e5),isN=nx&&nx.id===e.id,ck=!!P.done[e.id];
  tl+='<li class="'+(ck?'done ':'')+(past&&!ck?'past ':'')+(isN?'next':'')+'" style="--cc:'+CAT[e.cat][0]+'"><label class="plchk"><input type="checkbox" data-id="'+e.id+'"'+(ck?' checked':'')+'><span>'+IC('<path d="M5 12l5 5L20 7"/>',14)+'</span></label>'
   +'<span class="plti">'+IC(CAT[e.cat][1],16)+'</span><div class="pltx"><div class="plttop"><time>'+esc(e.d.getDate()+' '+D.mon[e.d.getMonth()].toLowerCase())+'</time>'
   +(isN?'<em class="b n">'+esc(U.nextc)+'</em>':'')+(past&&!ck?'<em class="b p">'+esc(U.past)+'</em>':'')+(!past&&dd<=60?'<em class="b s">'+esc(dd===0?U.today:rep(U.in_d,{n:dd}))+'</em>':'')+(e.exp?'<em class="b e">'+esc(U.exp)+'</em>':'')+'</div>'
   +'<b>'+(e.f?e.f+' ':'')+esc(e.t)+'</b>'+(e.n?'<small>'+esc(e.n)+'</small>':'')+(e.u?'<a href="'+esc(e.u)+'"'+(/^https?:/.test(e.u)?' target="_blank" rel="noopener"':'')+'>'+esc(U.more)+' →</a>':'')+'</div></li>'});
 tl+='</ol>';
 var tls='<section class="card plsec"><h3 class="plsh">'+IC('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>')+esc(U.tl_h)+'</h3><div class="pltlp"><span>'+esc(rep(U.tl_done,{a:dn,b:R.ev.length}))+'</span><i><b style="width:'+Math.round(dn/R.ev.length*100)+'%"></b></i></div>'+tl+'</section>';
 /* money */
 var mx=Math.max(a.b,Math.max.apply(null,R.sel.map(function(c){return c.ty})))*1.08||1;
 var mo='<section class="card plsec"><h3 class="plsh">'+IC(CAT.money[1])+esc(U.mo_h)+'</h3><div class="plmo2">'
  +R.sel.map(function(c){var st=a.b>=c.ty?'ok':a.b>=c.lo?'warn':'no';return '<div class="plmr '+st+'"><span>'+c.f+' '+esc(c.n)+'</span><div class="plmb"><i style="left:'+(c.lo/mx*100)+'%;width:'+Math.max(1.5,(c.ty-c.lo)/mx*100)+'%"></i><u style="left:'+(a.b/mx*100)+'%"></u></div><b>'+fmtUSD(c.lo)+'–'+fmtUSD(c.ty)+'</b></div>'}).join('')
  +'<div class="plml"><u></u> '+esc(U.mo_b)+': '+esc(D.bud.filter(function(b){return b.v===a.b})[0].big)+'</div></div><p class="note">'+esc(U.mo_note)+'</p><a class="btn s" href="'+esc(D.L.calc)+'">'+esc(U.k_money)+' →</a></section>';
 /* scholarships */
 var sl=[];R.sel.forEach(function(c){c.sl.forEach(function(s){sl.push([c,s])})});
 var sch='<section class="card plsec"><h3 class="plsh">'+IC('<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0zM17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>')+esc(U.sc_h)+'</h3>'
  +(sl.length?'<div class="plsl">'+sl.map(function(p){return '<a class="plsch" href="'+esc(p[1].u)+'" target="_blank" rel="noopener"><span>'+p[0].f+'</span><div><b>'+esc(p[1].n)+'</b><small>'+esc(p[1].cov)+'</small></div><em>↗</em></a>'}).join('')+'</div>':'')
  +(R.hasNeed?'<p class="plnote">'+esc(U.sc_need)+'</p>':'')
  +((a.x!=='none'&&!R.hasGov)?'<p class="plnote warn">'+esc(U.sc_warn)+' '+D.cs.filter(function(c){return c.sch==='gov'}).map(function(c){return c.f+' '+esc(c.n)}).join(', ')+'</p>':'')
  +'<a class="btn s" href="'+esc(D.L.sch)+'">'+esc(U.r_schol)+' →</a></section>';
 /* universities */
 var un=D.unis.filter(function(u){return R.sel.some(function(c){return c.k===u.k})});
 var uni='<section class="card plsec"><h3 class="plsh">'+IC(D.ai.strong)+esc(U.u_h)+'</h3>'
  +(un.length?'<div class="plun">'+un.map(function(u){return '<a href="'+esc(u.u)+'" target="_blank" rel="noopener"><span class="plseal" style="background:'+u.col+'">'+esc(u.s)+'</span><b>'+esc(u.n)+'</b><em>'+esc(U.u_reach)+'</em></a>'}).join('')+'</div>':'<p class="note">'+esc(U.u_none)+'</p>')
  +'<p class="plnote">'+esc(U.u_note)+'</p><a class="btn s" href="'+esc(D.L.top)+'">Top 10 →</a></section>';
 var tools='<div class="pltools"><button type="button" class="btn p" id="plprint">'+IC('<path d="M6 9V3h12v6M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><path d="M6 14h12v7H6z"/>',18)+esc(U.print)+'</button>'
  +'<button type="button" class="btn s" id="plshare">'+IC('<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.600 13.500l6.800 4M15.400 6.500l-6.800 4"/>',18)+esc(U.share)+'</button>'
  +'<button type="button" class="btn s" id="pledit">'+esc(U.edit)+'</button><button type="button" class="pllink" id="plreset">'+esc(U.reset)+'</button><span id="plmsg" class="plmsgx" role="status"></span></div>';
 r.innerHTML=hero+notes+tools+week+cc+ex+tls+mo+sch+uni;
 [].forEach.call(r.querySelectorAll('.pltl input'),function(b){b.onchange=function(){if(b.checked)P.done[b.dataset.id]=1;else delete P.done[b.dataset.id];save();var y=window.scrollY;show();window.scrollTo(0,y)}});
 $('plprint').onclick=function(){window.print()};
 $('pledit').onclick=function(){P.step=0;save();r.hidden=true;w.hidden=false;wiz();top()};
 $('plreset').onclick=function(){if(confirm(U.sure)){P={a:{},done:{},step:0,built:false};save();r.hidden=true;w.hidden=false;wiz();top()}};
 $('plshare').onclick=function(){
  var txt=U.r_for+': '+R.sel.map(function(c){return c.f+' '+c.n}).join(', ')+'\n'+U.ready+': '+R.score+'/100 ('+U['rl'+lv]+')\n'+U.r_start+': '+D.mon[8]+' '+R.start+'\nIELTS: '+(a.i||'—')+' → '+R.ieT.toFixed(1)+(R.satNeed?'\nSAT: '+(a.s||'—')+' → '+R.satT+'+':'')+'\n\n'+U.tl_h+':\n'
   +R.ev.filter(function(e){return e.d>=T0}).slice(0,8).map(function(e){return '• '+fd(e.d)+' — '+e.t}).join('\n')+'\n\n'+location.href;
  if(navigator.share){navigator.share({title:document.title,text:txt}).catch(function(){})}
  else if(navigator.clipboard){navigator.clipboard.writeText(txt).then(function(){$('plmsg').textContent=U.copied})}};
 top();
}
if(P.built&&P.a.c&&P.a.c.length&&P.a.x)show();else wiz();
})();

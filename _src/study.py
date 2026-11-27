# Study timer page (Pomodoro): focus/break timer, subject log, streak and weekly stats. All data stays on the device (localStorage).
import json
NAME = ("Oqıw taymeri", "Study timer", "O‘qish taymeri", "Таймер учёбы")
DESC = ("Oqıw taymeri (Pomodoro): fokus hám dem alıw, pánler boyınsha waqıt, kúnlik seriya hám háptelik statistika.",
        "Study timer (Pomodoro): focus and break sessions, time per subject, daily streak and weekly stats.",
        "O‘qish taymeri (Pomodoro): diqqat va tanaffus, fanlar bo‘yicha vaqt, kunlik seriya va haftalik statistika.",
        "Таймер учёбы (Pomodoro): фокус и перерывы, время по предметам, серия дней и статистика за неделю.")
LEAD = ("Dıqqat penen oqıń: 25 minut oqıw, 5 minut dem alıw. Hár kúni qansha oqıǵanıńız saqlanadı.",
        "Study with focus: 25 minutes of work, 5 minutes of rest. Your daily study time is saved on this phone.",
        "Diqqat bilan o‘qing: 25 daqiqa ish, 5 daqiqa dam. Kunlik o‘qish vaqtingiz shu telefonda saqlanadi.",
        "Учитесь сосредоточенно: 25 минут работы, 5 минут отдыха. Ваше время учёбы сохраняется на этом телефоне.")
UI = {
 "focus": ("Dıqqat", "Focus", "Diqqat", "Фокус"), "brk": ("Dem alıw", "Break", "Tanaffus", "Перерыв"),
 "start": ("Baslaw", "Start", "Boshlash", "Старт"), "pause": ("Pauza", "Pause", "Pauza", "Пауза"), "resume": ("Dawam etiw", "Resume", "Davom etish", "Продолжить"),
 "reset": ("Qaytadan", "Reset", "Qayta", "Сброс"), "skip": ("Dem alıwdı ótkiziw", "Skip break", "Tanaffusni o‘tkazish", "Пропустить перерыв"),
 "subj": ("Pán", "Subject", "Fan", "Предмет"), "gen": ("Ulıwma", "General", "Umumiy", "Общее"),
 "wake": ("Ekrandı óshirmew", "Keep screen on", "Ekranni o‘chirmaslik", "Не выключать экран"),
 "presets": ("Tayın rejimler", "Presets", "Tayyor rejimlar", "Режимы"),
 "today": ("Búgin", "Today", "Bugun", "Сегодня"), "min": ("min", "min", "daq", "мин"), "sess": ("sessiya", "sessions", "sessiya", "сессий"),
 "streak": ("Seriya", "Streak", "Seriya", "Серия"), "days": ("kún", "days", "kun", "дн."),
 "week": ("Sońǵı 7 kún", "Last 7 days", "So‘nggi 7 kun", "Последние 7 дней"), "bysubj": ("Pánler boyınsha (7 kún)", "By subject (7 days)", "Fanlar bo‘yicha (7 kun)", "По предметам (7 дней)"),
 "none": ("Házirshe jazıw joq. Birinshi sessiyanı baslań!", "Nothing yet. Start your first session!", "Hozircha yozuv yo‘q. Birinchi sessiyani boshlang!", "Пока пусто. Начните первую сессию!"),
 "doneF": ("Sessiya tamamlandı! Endi dem alıń.", "Session complete! Time for a break.", "Sessiya tugadi! Endi dam oling.", "Сессия завершена! Пора отдохнуть."),
 "doneB": ("Dem alıw tamamlandı. Dawam etemiz be?", "Break over. Ready for the next one?", "Tanaffus tugadi. Davom etamizmi?", "Перерыв окончен. Продолжим?"),
 "tip": ("Kúshli usıl: telefondı shetke qoyıń hám tek bir pán ústinde islewge háreket etiń.", "Tip: put your phone aside and work on one subject only.", "Maslahat: telefonni chetga qo‘ying va faqat bitta fan ustida ishlang.", "Совет: отложите телефон и занимайтесь только одним предметом."),
 "clear": ("Statistikanı óshiriw", "Clear stats", "Statistikani o‘chirish", "Очистить статистику"), "sure": ("Barlıq statistika óshiriledi. Dawam etemiz be?", "All stats will be deleted. Continue?", "Barcha statistika o‘chiriladi. Davom etamizmi?", "Вся статистика будет удалена. Продолжить?"),
 "dn": (("Ye", "Du", "Se", "Ch", "Pa", "Ju", "Sh"), ("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"), ("Ya", "Du", "Se", "Ch", "Pa", "Ju", "Sh"), ("Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб")),
}
PRESETS = [(25, 5), (45, 10), (50, 10), (15, 3)]
JS = r"""
(function(){
  var D=JSON.parse(document.getElementById('stdata').textContent),X=D.t,S=D.subj;
  var $=function(id){return document.getElementById(id)};
  var KEY='studyTimer',st={log:{},cfg:{f:25,b:5,s:''},run:null};
  try{var raw=localStorage.getItem(KEY);if(raw){var o=JSON.parse(raw);if(o&&typeof o==='object')st=Object.assign(st,o)}}catch(e){}
  function save(){try{localStorage.setItem(KEY,JSON.stringify(st))}catch(e){}}
  function dk(d){d=d||new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
  function esc(s){return String(s).replace(/[&<>"']/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]})}
  function fmt(ms){var s=Math.max(0,Math.ceil(ms/1000)),m=Math.floor(s/60);return ('0'+m).slice(-2)+':'+('0'+(s%60)).slice(-2)}
  var C=2*Math.PI*90,ring=$('string');ring.style.strokeDasharray=C;
  var wl=null;
  function wake(on){try{if(on&&navigator.wakeLock){navigator.wakeLock.request('screen').then(function(l){wl=l}).catch(function(){})}else if(wl){wl.release();wl=null}}catch(e){}}
  function beep(){try{var A=window.AudioContext||window.webkitAudioContext,c=new A();[0,.28,.56].forEach(function(t){var o=c.createOscillator(),g=c.createGain();o.frequency.value=880;o.connect(g);g.connect(c.destination);g.gain.setValueAtTime(.0001,c.currentTime+t);g.gain.exponentialRampToValueAtTime(.25,c.currentTime+t+.02);g.gain.exponentialRampToValueAtTime(.0001,c.currentTime+t+.22);o.start(c.currentTime+t);o.stop(c.currentTime+t+.25)});}catch(e){}
    try{if(navigator.vibrate)navigator.vibrate([200,100,200,100,200])}catch(e){}}
  // subjects select
  var sel=$('stsubj');sel.innerHTML='<option value="">'+esc(X.gen)+'</option>'+S.map(function(s,i){return '<option value="'+i+'">'+esc(s.n)+'</option>'}).join('');sel.value=st.cfg.s;
  sel.onchange=function(){st.cfg.s=sel.value;save()};
  // presets
  var pb=$('stpre');pb.innerHTML=D.p.map(function(p,i){return '<button type="button" data-i="'+i+'"><b>'+p[0]+'</b>/'+p[1]+'</button>'}).join('');
  function markPre(){[].forEach.call(pb.children,function(b){var p=D.p[+b.dataset.i];b.classList.toggle('on',p[0]===st.cfg.f&&p[1]===st.cfg.b)})}
  pb.onclick=function(e){var b=e.target.closest('button');if(!b||st.run)return;var p=D.p[+b.dataset.i];st.cfg.f=p[0];st.cfg.b=p[1];save();markPre();draw()};
  function addLog(min){if(min<=0)return;var k=dk(),d=st.log[k]||(st.log[k]={}),key=st.run&&st.run.s!=null?st.run.s:st.cfg.s;key=key===''?'g':key;d[key]=(d[key]||0)+min;d.n=(d.n||0)+1;save()}
  function begin(mode){var dur=(mode==='focus'?st.cfg.f:st.cfg.b)*60000;st.run={m:mode,end:Date.now()+dur,dur:dur,p:null,s:st.cfg.s};save();wake($('stwake').checked&&mode==='focus')}
  function finish(){var r=st.run;if(!r)return;if(r.m==='focus'){addLog(Math.round(r.dur/60000));st.run=null;beep();$('stmsg').textContent=X.doneF;begin('break')}else{st.run=null;beep();$('stmsg').textContent=X.doneB;wake(false)}save();stats();draw()}
  $('stgo').onclick=function(){var r=st.run;$('stmsg').textContent='';if(!r){begin('focus')}else if(r.p!=null){r.end=Date.now()+r.p;r.p=null;save()}else{r.p=Math.max(0,r.end-Date.now());save()}draw()};
  $('streset').onclick=function(){st.run=null;save();wake(false);$('stmsg').textContent='';draw()};
  $('stskip').onclick=function(){st.run=null;save();$('stmsg').textContent='';draw()};
  $('stwake').checked=!!st.cfg.w;$('stwake').onchange=function(){st.cfg.w=this.checked;save();wake(this.checked&&st.run&&st.run.m==='focus'&&st.run.p==null)};
  document.addEventListener('visibilitychange',function(){if(!document.hidden&&st.run&&st.run.p==null&&$('stwake').checked&&st.run.m==='focus')wake(true)});
  function draw(){
    var r=st.run,left,dur,mode;
    if(r){dur=r.dur;left=r.p!=null?r.p:r.end-Date.now();mode=r.m}else{mode='focus';dur=st.cfg.f*60000;left=dur}
    if(r&&r.p==null&&left<=0){finish();return}
    $('sttime').textContent=fmt(left);$('stmode').textContent=mode==='focus'?X.focus:X.brk;
    ring.style.strokeDashoffset=C*(1-(dur?left/dur:1));
    $('stcard').className='card stmain '+(mode==='break'?'isbreak':'')+(r&&r.p==null?' running':'');
    $('stgo').textContent=!r?X.start:r.p!=null?X.resume:X.pause;
    $('streset').hidden=!r;$('stskip').hidden=!(r&&r.m==='break');
    sel.disabled=!!r;pb.classList.toggle('lock',!!r);
    document.title=r&&r.p==null?fmt(left)+' · '+(mode==='focus'?X.focus:X.brk):D.title;
  }
  function stats(){
    var t=dk(),td=st.log[t]||{},sum=function(o){var n=0;for(var k in o)if(k!=='n')n+=o[k];return n};
    $('sttod').textContent=sum(td);$('stsess').textContent=td.n||0;
    var sk=0,d=new Date();if(!sum(st.log[dk(d)]||{}))d.setDate(d.getDate()-1);
    while(sum(st.log[dk(d)]||{})>0){sk++;d.setDate(d.getDate()-1)}
    $('stst').textContent=sk;
    var days=[],mx=1,per={},any=false;
    for(var i=6;i>=0;i--){var dd=new Date();dd.setDate(dd.getDate()-i);var l=st.log[dk(dd)]||{},m=sum(l);days.push({d:dd,m:m});if(m>mx)mx=m;if(m)any=true;for(var k in l)if(k!=='n'){per[k]=(per[k]||0)+l[k]}}
    $('stbars').innerHTML=days.map(function(x,i){var h=Math.round(x.m/mx*100);return '<div class="stbar'+(i===6?' tdy':'')+'"><span class="stbv">'+(x.m||'')+'</span><i style="height:'+Math.max(h,x.m?6:2)+'%"></i><small>'+X.dn[x.d.getDay()]+'</small></div>'}).join('');
    var keys=Object.keys(per).sort(function(a,b){return per[b]-per[a]}),tot=keys.reduce(function(a,k){return a+per[k]},0)||1;
    $('stsubjs').innerHTML=any?keys.map(function(k){var s=k==='g'?{n:X.gen,c:'#64748b'}:S[+k]||{n:X.gen,c:'#64748b'};return '<li style="--sc:'+s.c+'"><span>'+esc(s.n)+'</span><div class="stbarh"><i style="width:'+Math.round(per[k]/tot*100)+'%"></i></div><b>'+per[k]+' '+X.min+'</b></li>'}).join(''):'<li class="none">'+esc(X.none)+'</li>';
  }
  $('stclear').onclick=function(){if(confirm(X.sure)){st.log={};save();stats()}};
  markPre();stats();draw();setInterval(function(){if(st.run&&st.run.p==null)draw()},250);
})();
"""

def body(i, up, subjects):
    t = {k: (v[i] if k != "dn" else list(v[i])) for k, v in UI.items()}
    data = json.dumps({"t": t, "subj": [{"n": n[i], "c": c} for n, c in subjects], "p": PRESETS, "title": NAME[i]}, ensure_ascii=False)
    ring = '<svg viewBox="0 0 200 200" class="stsvg" aria-hidden="true"><circle cx="100" cy="100" r="90" class="strb"/><circle id="string" cx="100" cy="100" r="90" class="strf" transform="rotate(-90 100 100)"/></svg>'
    html = (f'<p class="lead2">{LEAD[i]}</p><div class="stwrap">'
            f'<div class="card stmain" id="stcard"><div class="stpre" id="stpre" role="group" aria-label="{UI["presets"][i]}"></div>'
            f'<div class="stringw">{ring}<div class="strt"><small id="stmode"></small><b id="sttime">25:00</b></div></div>'
            f'<label class="stl" for="stsubj">{UI["subj"][i]}</label><select id="stsubj"></select>'
            f'<div class="stbtns"><button type="button" class="btn p" id="stgo">{UI["start"][i]}</button><button type="button" class="btn s" id="streset" hidden>{UI["reset"][i]}</button><button type="button" class="btn s" id="stskip" hidden>{UI["skip"][i]}</button></div>'
            f'<label class="stwl"><input type="checkbox" id="stwake"> {UI["wake"][i]}</label><p class="stmsg" id="stmsg" role="status"></p><p class="note">{UI["tip"][i]}</p></div>'
            f'<div class="card ststats"><div class="sttiles"><div><b id="sttod">0</b><span>{UI["today"][i]} · {UI["min"][i]}</span></div><div><b id="stsess">0</b><span>{UI["sess"][i]}</span></div><div><b id="stst">0</b><span>{UI["streak"][i]} · {UI["days"][i]}</span></div></div>'
            f'<h3>{UI["week"][i]}</h3><div class="stbars" id="stbars"></div><h3>{UI["bysubj"][i]}</h3><ul class="stsubjs" id="stsubjs"></ul>'
            f'<button type="button" class="stclr" id="stclear">{UI["clear"][i]}</button></div></div>'
            f'<script id="stdata" type="application/json">{data}</script><script>{JS}</script>')
    return html

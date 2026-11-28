(function(){var bs=document.querySelectorAll('.ngb');function close(x){bs.forEach(function(b){if(b!==x){b.setAttribute('aria-expanded','false');b.nextElementSibling.hidden=true}})}
    bs.forEach(function(b){b.addEventListener('click',function(e){e.stopPropagation();var o=b.getAttribute('aria-expanded')==='true';close(b);b.setAttribute('aria-expanded',!o);b.nextElementSibling.hidden=o})});
    document.addEventListener('click',function(e){if(!e.target.closest('.ng'))close()});document.addEventListener('keydown',function(e){if(e.key==='Escape')close()})})();

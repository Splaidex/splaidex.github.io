---
hide:
  - navigation
  - toc
---

<div id="terminal">
  <div id="terminal-body">
    <p class="t-line"><span class="t-prompt">splaidex@portfolio:~$</span> <span class="t-cmd" id="cmd1"></span><span class="t-cursor" id="cur1">█</span></p>
    <div id="output1" style="display:none">
      <p class="t-output">Python developer. Vibe-coder. Builder.</p>
    </div>
    <p class="t-line" id="line2" style="display:none"><span class="t-prompt">splaidex@portfolio:~$</span> <span class="t-cmd" id="cmd2"></span><span class="t-cursor" id="cur2">█</span></p>
    <div id="output2" style="display:none">
      <p class="t-output">PyQt6 · Telegram Bots · API · CUDA · Automation</p>
    </div>
    <p class="t-line" id="line3" style="display:none"><span class="t-prompt">splaidex@portfolio:~$</span> <span class="t-cmd" id="cmd3"></span><span class="t-cursor" id="cur3">█</span></p>
    <div id="output3" style="display:none">
      <p class="t-output"><a href="projects/" class="t-link">[ projects ]</a> &nbsp; <a href="about/" class="t-link">[ about me ]</a></p>
    </div>
  </div>
</div>

<style>
#terminal {
  max-width: 760px;
  margin: 6rem auto;
  padding: 2rem;
  border: 1px solid #cc000044;
  background: #000;
  box-shadow: 0 0 40px #cc000022;
}

.t-line {
  margin: 0.4rem 0;
  font-family: 'Share Tech Mono', monospace;
  font-size: 1.1rem;
}

.t-prompt {
  color: #cc0000;
}

.t-cmd {
  color: #ffffff;
}

.t-cursor {
  color: #cc0000;
  animation: blink 1s step-end infinite;
}

.t-output {
  color: #aaaaaa;
  font-family: 'Share Tech Mono', monospace;
  font-size: 1rem;
  margin: 0.2rem 0 0.8rem 1rem;
  padding: 0;
}

.t-link {
  color: #cc0000 !important;
  border: none !important;
  text-shadow: 0 0 8px #cc000066;
  transition: all 0.2s;
}

.t-link:hover {
  color: #ff4444 !important;
  text-shadow: 0 0 12px #cc0000aa;
}

@keyframes blink {
  50% { opacity: 0; }
}
</style>

<script>
function typeText(elementId, text, speed, callback) {
  let i = 0;
  const el = document.getElementById(elementId);
  const interval = setInterval(() => {
    el.textContent += text[i];
    i++;
    if (i >= text.length) {
      clearInterval(interval);
      if (callback) callback();
    }
  }, speed);
}

function hideCursor(id) {
  const el = document.getElementById(id);
  if (el) el.style.display = 'none';
}

function showEl(id) {
  document.getElementById(id).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function() {
  setTimeout(() => {
    typeText('cmd1', 'whoami', 80, () => {
      hideCursor('cur1');
      showEl('output1');
      setTimeout(() => {
        showEl('line2');
        typeText('cmd2', 'cat skills.txt', 80, () => {
          hideCursor('cur2');
          showEl('output2');
          setTimeout(() => {
            showEl('line3');
            typeText('cmd3', 'ls ./portfolio', 80, () => {
              hideCursor('cur3');
              showEl('output3');
            });
          }, 400);
        });
      }, 400);
    });
  }, 800);
});
</script>
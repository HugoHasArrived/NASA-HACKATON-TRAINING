from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)
PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<meta name="theme-color" content="#060914">
<title>Lunar Path — Space Mission Game</title>
<style>
:root{color-scheme:dark;--bg:#060914;--panel:#101a2e;--line:#344563;--text:#eef6ff;--muted:#a7bad6;--cyan:#66e7ff;--gold:#ffd874;--green:#78f0b1;--red:#ff6c83}
*{box-sizing:border-box}html,body{padding:0;margin:0;min-height:100%;background:radial-gradient(ellipse at 50% -15%,#213d68 0,#0c1428 45%,#05070f 100%);color:var(--text);font-family:Inter,Segoe UI,Arial,sans-serif}body{min-height:100vh}button,input,select{font:inherit}button{border:1px solid #425a7b;background:#1b2e4b;color:var(--text);padding:11px 15px;border-radius:10px;font-weight:800;cursor:pointer;touch-action:manipulation}button:hover{border-color:var(--cyan);background:#294667}button:disabled{opacity:.45;cursor:not-allowed}button:focus-visible,select:focus-visible{outline:3px solid var(--gold);outline-offset:2px}.shell{width:min(1320px,calc(100% - 20px));margin:auto;padding:12px 0 22px}.top{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:10px}.brand{display:flex;align-items:center;gap:10px}.mark{width:42px;height:42px;display:grid;place-items:center;border-radius:13px;background:linear-gradient(135deg,#67eeff,#a4acff);color:#07101b;font-size:23px;font-weight:1000;box-shadow:0 0 30px #62dfff45}.brand h1{font-size:14px;letter-spacing:.18em;margin:0}.brand p{font-size:10px;color:var(--muted);letter-spacing:.15em;margin:4px 0 0}.headright{display:flex;align-items:center;gap:8px;flex-wrap:wrap;justify-content:flex-end}.badge{border:1px solid var(--line);border-radius:30px;background:#0a1120;padding:8px 10px;font-size:10px;color:var(--muted);letter-spacing:.08em}.layout{display:grid;grid-template-columns:minmax(0,1fr) 270px;gap:10px;align-items:start}.screen{position:relative;min-width:0;background:#060a16;border:1px solid #2d4365;border-radius:17px;overflow:hidden;box-shadow:0 20px 60px #0008}.canvaswrap{position:relative;aspect-ratio:16/9;min-height:300px;max-height:calc(100vh - 180px);background:#050916}.canvaswrap canvas{display:block;width:100%;height:100%;object-fit:contain;image-rendering:pixelated;touch-action:none}.hud{position:absolute;inset:0;pointer-events:none;display:flex;flex-direction:column;justify-content:space-between;padding:12px}.hudtop,.hudbottom{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}.hudbottom{align-items:flex-end}.hudcard{background:#050b18c9;border:1px solid #344867;border-radius:10px;padding:8px 10px;backdrop-filter:blur(5px);max-width:75%}.hudlabel{font-size:9px;letter-spacing:.18em;text-transform:uppercase;color:var(--cyan);font-weight:900}.hudvalue{font-size:13px;font-weight:850;margin-top:4px}.hudsmall{font-size:10px;color:#c1cde0;line-height:1.5;margin-top:3px}.meterrow{display:flex;gap:6px;align-items:center;margin-top:5px;font-size:9px;color:var(--muted)}.meter{width:95px;height:5px;border-radius:10px;background:#293850;overflow:hidden}.meter span{display:block;height:100%;width:70%;background:linear-gradient(90deg,#5de5fa,#91a8ff)}.sidebar{background:linear-gradient(145deg,#121e34,#0a1222);border:1px solid #2b405f;border-radius:15px;padding:13px;min-width:0}.sidehead{display:flex;align-items:center;justify-content:space-between;gap:8px;margin:0 0 10px}.sidehead h2{font-size:13px;letter-spacing:.05em;margin:0}.sidebadge{font-size:9px;color:var(--cyan);border:1px solid #35506d;border-radius:30px;padding:6px 8px}.statgrid{display:grid;grid-template-columns:1fr 1fr;gap:7px}.stat{padding:10px;background:#091224;border:1px solid #263b59;border-radius:10px}.stat strong{font-size:18px;color:var(--cyan);display:block}.stat span{font-size:9px;color:var(--muted)}.side-section{border-top:1px solid #293a55;margin-top:13px;padding-top:12px}.side-section h3{font-size:11px;margin:0 0 8px;letter-spacing:.08em;text-transform:uppercase;color:#d4e4f7}.objective{font-size:11px;color:var(--muted);line-height:1.55}.objectiveline{display:flex;gap:8px;align-items:flex-start;margin:7px 0}.dot{width:18px;height:18px;display:grid;place-items:center;background:#1d2f49;border:1px solid #405879;border-radius:6px;color:var(--cyan);font-size:10px;flex:none}.controlsnote{font-size:10px;color:var(--muted);line-height:1.7}.log{font:10px/1.6 ui-monospace,SFMono-Regular,Consolas,monospace;color:#a9c9ec;white-space:pre-wrap;overflow-wrap:anywhere;min-height:75px;max-height:155px;overflow:auto;background:#050a14;border:1px solid #263a54;border-radius:9px;padding:8px}.actionsbar{display:flex;gap:8px;flex-wrap:wrap;margin-top:9px}.actionsbar button{font-size:11px;padding:9px 10px}.primary{color:#071322;background:linear-gradient(100deg,#5fe5f8,#abb3ff);border:0}.danger{background:#451a29;border-color:#7f3b4a}.hidden{display:none!important}.overlay{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:#040817c9;backdrop-filter:blur(4px);padding:16px;z-index:5;overflow:auto}.modal{width:min(700px,100%);max-height:100%;overflow:auto;border:1px solid #3b5275;border-radius:17px;background:linear-gradient(145deg,#16243c,#0a1223);box-shadow:0 25px 90px #000b;padding:22px}.modal.slim{width:min(550px,100%)}.eyebrow{font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--cyan);font-weight:900}.modal h2{font-size:clamp(27px,4vw,43px);line-height:1.08;margin:10px 0}.modal p{color:var(--muted);font-size:13px;line-height:1.65}.modal .bar{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}.featuregrid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:16px}.feature{padding:12px;background:#091426;border:1px solid #2d4260;border-radius:11px}.feature strong{display:block;color:var(--cyan);font-size:15px}.feature span{display:block;color:var(--muted);font-size:10px;line-height:1.5;margin-top:5px}.design-grid{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:14px}.module{background:#091427;border:1px solid #2e4260;border-radius:11px;padding:10px;min-width:0}.module label{display:block;font-size:11px;font-weight:850;margin-bottom:7px}.module select{width:100%;border:1px solid #354d6e;border-radius:8px;padding:9px;background:#101c31;color:var(--text);font-size:11px}.moddetail{font-size:10px;color:var(--muted);line-height:1.5;margin-top:6px}.designsummary{display:grid;grid-template-columns:repeat(3,1fr);gap:7px;margin-top:12px}.designstat{padding:10px;border:1px solid #304563;background:#091324;border-radius:9px}.designstat strong{font-size:18px;color:var(--cyan);display:block}.designstat small{font-size:9px;color:var(--muted)}.message{border:1px solid #3c5272;background:#0a1426;padding:10px;border-radius:10px;font-size:11px;line-height:1.55;margin-top:11px}.message.good{border-color:#326f55;color:#b8f4d5}.message.bad{border-color:#87384b;color:#ffc0ca}.mobilepad{display:none;grid-template-columns:repeat(3,45px);grid-template-rows:repeat(2,40px);gap:4px;justify-content:center;align-items:center;margin:9px auto 0}.mobilepad button{padding:0;min-width:44px;height:40px;background:#12213a;font-size:17px;user-select:none;-webkit-user-select:none}.mobilepad .up{grid-column:2;grid-row:1}.mobilepad .left{grid-column:1;grid-row:2}.mobilepad .down{grid-column:2;grid-row:2}.mobilepad .right{grid-column:3;grid-row:2}.mobilepad .action{grid-column:3;grid-row:1;font-size:10px;color:var(--gold)}.footer{text-align:center;color:#7285a4;font-size:10px;padding:13px}.helpband{font-size:10px;color:#a8b9d4;text-align:center;margin-top:8px;line-height:1.5}.success{color:#bbf8d7}.failure{color:#ffbac7}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
@media(max-width:920px){.layout{grid-template-columns:1fr}.sidebar{display:grid;grid-template-columns:1fr 1fr;gap:10px}.side-section{margin:0;border-top:0;padding-top:0}.side-section:last-child{grid-column:1/-1}.canvaswrap{max-height:none;min-height:0}.mobilepad{display:grid}}
@media(max-width:580px){.shell{width:calc(100% - 10px);padding-top:7px}.top{align-items:flex-start}.mark{width:35px;height:35px}.brand h1{font-size:12px}.brand p{font-size:8px}.badge{font-size:8px;padding:7px}.headright button{font-size:10px;padding:7px}.sidebar{display:block;padding:10px}.side-section{margin-top:11px;padding-top:10px;border-top:1px solid #293a55}.side-section:last-child{display:block}.hud{padding:5px}.hudcard{padding:6px;max-width:68%}.hudlabel{font-size:7px}.hudvalue{font-size:10px}.hudsmall{font-size:8px}.meter{width:55px}.modal{padding:15px}.modal h2{font-size:29px}.featuregrid{grid-template-columns:1fr}.design-grid{grid-template-columns:1fr}.designsummary{grid-template-columns:repeat(3,1fr)}.designstat{padding:7px}.designstat strong{font-size:15px}.canvaswrap{aspect-ratio:4/3}.mobilepad{margin-top:8px}}
</style>
</head>
<body>
<div class="shell">
<header class="top"><div class="brand"><div class="mark">✦</div><div><h1>LUNAR PATH</h1><p>SPACE MISSION DESIGN GAME</p></div></div><div class="headright"><span class="badge" id="topStatus">MISSION CONTROL STANDBY</span><button id="restartTop">Restart</button></div></header>
<div class="layout">
<main class="screen">
<div class="canvaswrap"><canvas id="gameCanvas" width="1000" height="562" aria-label="Playable Lunar Path space mission game"></canvas>
<div class="hud hidden" id="hud"><div class="hudtop"><div class="hudcard"><div class="hudlabel" id="hudPhase">FLIGHT SIMULATOR</div><div class="hudvalue" id="hudObjective">Reach the checkpoints</div><div class="hudsmall" id="hudHint">Use arrow keys or WASD</div></div><div class="hudcard"><div class="hudlabel">Mission telemetry</div><div class="hudvalue" id="hudTelemetry">INTEGRITY 100%</div><div class="meterrow">FUEL <div class="meter"><span id="fuelMeter"></span></div><strong id="fuelValue">100%</strong></div><div class="meterrow">POWER <div class="meter"><span id="powerMeter"></span></div><strong id="powerValue">100%</strong></div></div></div><div class="hudbottom"><div class="hudcard"><div class="hudlabel">Mission log</div><div class="hudsmall" id="hudLog">Mission systems nominal.</div></div><div class="hudcard"><div class="hudlabel">Current phase</div><div class="hudvalue" id="hudPhaseNumber">01 / 07</div></div></div></div>
<div class="overlay" id="overlay"><div class="modal"><div class="eyebrow">Interactive lunar expedition</div><h2>Fly to the Moon.<br>Bring your crew home.</h2><p>This is a real-time playable mission, not a multiple-choice test. Pilot the training craft, build your spacecraft, control launch, time your lunar transfer, land manually, explore the surface, then fly the capsule through Earth’s atmosphere.</p><div class="featuregrid"><div class="feature"><strong>✦ Pilot</strong><span>Steer through the flight simulator checkpoints and dodge debris.</span></div><div class="feature"><strong>🚀 Build</strong><span>Trade budget, mass, power, fuel and redundancy.</span></div><div class="feature"><strong>🌕 Explore</strong><span>Make a controlled landing, collect samples, and return safely.</span></div></div><div class="message">One critical mistake can end the mission. Unsafe spacecraft design, a debris collision, failed landing, bad orbital burn, or unsafe atmospheric entry triggers the opposite ending. Correct flight and a successful recovery bring the crew home.</div><div class="bar"><button class="primary" id="beginButton">Begin mission →</button><button id="briefButton">Controls & briefing</button></div></div></div>
</div>
<div class="mobilepad" id="mobilepad"><button class="up" data-key="ArrowUp">▲</button><button class="left" data-key="ArrowLeft">◀</button><button class="down" data-key="ArrowDown">▼</button><button class="right" data-key="ArrowRight">▶</button><button class="action" data-key="Space">ACTION</button></div>
<div class="helpband" id="controlSummary">Keyboard: WASD / arrows to move · Space to thrust, jump, ignite, or confirm a timed action</div>
</main>
<aside class="sidebar">
<div><div class="sidehead"><h2>MISSION STATUS</h2><span class="sidebadge" id="phaseBadge">STANDBY</span></div><div class="statgrid"><div class="stat"><strong id="integrityStat">100%</strong><span>Vehicle integrity</span></div><div class="stat"><strong id="crewStat">READY</strong><span>Crew status</span></div><div class="stat"><strong id="sampleStat">0 / 3</strong><span>Lunar samples</span></div><div class="stat"><strong id="scoreStat">0</strong><span>Mission score</span></div></div></div>
<div class="side-section"><h3>Mission objectives</h3><div class="objective" id="objectiveList"><div class="objectiveline"><span class="dot">1</span><span>Complete flight training.</span></div><div class="objectiveline"><span class="dot">2</span><span>Assemble a safe spacecraft.</span></div><div class="objectiveline"><span class="dot">3</span><span>Launch, land, gather science, and return.</span></div></div></div>
<div class="side-section"><h3>Mission control log</h3><div class="log" id="missionLog">[00:00] Lunar Path simulator initialized.
[00:01] Awaiting crew commander.</div><div class="actionsbar"><button id="soundButton">Sound: on</button><button id="pauseButton">Pause</button></div></div>
</aside>
</div>
<div class="footer">LUNAR PATH · Original educational space mission game · Fictional arcade physics, not real flight guidance</div>
</div>
<script>
const canvas=document.getElementById('gameCanvas');
const ctx=canvas.getContext('2d');
const $=id=>document.getElementById(id);
const WIDTH=1000;
const HEIGHT=562;
const FLOOR=484;
const held=new Set();
let worldAtlas=[];
let animationId=0;
let previousTime=0;
let paused=false;
let soundEnabled=true;
let audioContext=null;
let game;
const phaseTitles={menu:'Mission control',training:'Flight training',design:'Spacecraft assembly',launch:'Launch and ascent',orbit:'Lunar transfer',landing:'Moon landing',science:'Lunar exploration',entry:'Earth return',win:'Mission complete',fail:'Mission failure'};
const phases=['training','design','launch','orbit','landing','science','entry'];
const moduleOptions={
engine:[{id:'balanced',name:'Balanced chemical engine',mass:20,cost:22,safe:true,fuel:100,desc:'Reliable thrust, manageable mass and enough performance for the expedition.'},{id:'efficient',name:'High-efficiency engine',mass:24,cost:30,safe:true,fuel:115,desc:'More expensive and slightly heavier, but improves propellant efficiency.'},{id:'weak',name:'Underpowered prototype',mass:11,cost:12,safe:false,fuel:55,desc:'Cannot provide the required maneuver margin for a crewed lunar trip.'}],
lander:[{id:'two_stage',name:'Two-stage lunar lander',mass:18,cost:20,safe:true,desc:'Includes descent and ascent capability for a controlled Moon landing.'},{id:'capsule',name:'Crew capsule only',mass:10,cost:12,safe:false,desc:'A capsule alone cannot safely perform this game’s lunar surface mission.'},{id:'none',name:'No lunar lander',mass:0,cost:0,safe:false,desc:'There is no safe way to reach the lunar surface and return to orbit.'}],
shield:[{id:'full',name:'Full ablative heat shield',mass:8,cost:10,safe:true,desc:'A full heat shield protects the return capsule during entry.'},{id:'partial',name:'Incomplete thermal tiles',mass:4,cost:4,safe:false,desc:'The return capsule has an unprotected thermal section.'}],
power:[{id:'solar',name:'Solar array + reserve battery',mass:8,cost:10,safe:true,desc:'Solar power and stored energy cover critical systems and reserves.'},{id:'battery',name:'Single short-duration battery',mass:4,cost:4,safe:false,desc:'Power may be lost during the extended mission.'}],
life:[{id:'redundant',name:'Redundant life-support loops',mass:8,cost:12,safe:true,desc:'Backup life support preserves the crew if a primary loop fails.'},{id:'single',name:'Single life-support loop',mass:4,cost:4,safe:false,desc:'A single failure would remove a critical crew-protection function.'}],
comms:[{id:'highgain',name:'High-gain antenna + backup link',mass:5,cost:8,safe:true,desc:'Long-distance communications include a backup path.'},{id:'lowgain',name:'Low-gain antenna only',mass:2,cost:3,safe:false,desc:'The link is not sufficiently robust for this mission profile.'}],
rover:[{id:'none',name:'No science rover',mass:0,cost:0,safe:true,desc:'Collect portable samples by hand; lowest mass and cost.'},{id:'rover',name:'Compact science rover',mass:9,cost:7,safe:true,desc:'Adds surface mobility and a science bonus but increases mass.'}],
spectrometer:[{id:'standard',name:'Compact spectrometer',mass:0,cost:0,safe:true,desc:'Standard orbital and surface observations.'},{id:'advanced',name:'Advanced spectrometer',mass:4,cost:6,safe:true,desc:'More detailed readings, trading cost and mass for science value.'}]
};
function freshGame(){return {scene:'menu',time:0,elapsed:0,integrity:100,fuel:100,power:100,budget:100,mass:0,score:0,samples:0,log:['[00:00] Lunar Path simulator initialized.','[00:01] Awaiting crew commander.'],camera:0,paused:false,failed:false,phaseStarted:0,training:{x:100,y:420,speed:3.5,target:0,targets:[{x:250,y:150},{x:710,y:125},{x:825,y:390}],hazards:[{x:440,y:290,r:22,speed:1.2,phase:0.3},{x:640,y:360,r:17,speed:1.65,phase:1.9},{x:360,y:110,r:14,speed:1.1,phase:4.1}]},design:{engine:'balanced',lander:'two_stage',shield:'full',power:'solar',life:'redundant',comms:'highgain',rover:'none',spectrometer:'standard'},launch:{ignited:false,altitude:0,throttle:75,angle:0,outOfBand:0},orbit:{time:0,angle:0,ready:false,cycles:0},landing:{x:500,y:100,vx:0,vy:0.15,fuel:100,landed:false},science:{x:90,y:FLOOR-18,vx:0,vy:0,camera:0,got:[],worldWidth:3000},entry:{time:0,angle:0,deployed:false,stable:0},report:'',paused:false};}
function logLine(message){const s=Math.floor(game.elapsed);const stamp=String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');game.log.push('['+stamp+'] '+message);game.log=game.log.slice(-14);$('missionLog').textContent=game.log.join('\n');$('hudLog').textContent=message;}
function tone(frequency=440,duration=.07,type='sine',volume=.035){if(!soundEnabled)return;try{audioContext=audioContext||new(window.AudioContext||window.webkitAudioContext)();const oscillator=audioContext.createOscillator();const gain=audioContext.createGain();oscillator.type=type;oscillator.frequency.value=frequency;gain.gain.value=volume;gain.gain.exponentialRampToValueAtTime(.001,audioContext.currentTime+duration);oscillator.connect(gain);gain.connect(audioContext.destination);oscillator.start();oscillator.stop(audioContext.currentTime+duration);}catch(e){}}
function setScene(scene){game.scene=scene;game.phaseStarted=game.elapsed;const active=scene!=='menu'&&scene!=='win'&&scene!=='fail';$('hud').classList.toggle('hidden',!active);$('topStatus').textContent=phaseTitles[scene]||'MISSION ACTIVE';$('phaseBadge').textContent=scene.toUpperCase();$('hudPhase').textContent=(phaseTitles[scene]||scene).toUpperCase();$('hudPhaseNumber').textContent=String(Math.max(1,phases.indexOf(scene)+1)).padStart(2,'0')+' / 07';$('overlay').classList.add('hidden');held.clear();if(scene==='training'){ $('hudObjective').textContent='Reach all 3 green checkpoints';$('hudHint').textContent='WASD / arrows to fly · avoid red debris';$('controlSummary').textContent='TRAINING: WASD or arrows to steer the blue craft; hit each green beacon and avoid red debris.'; }if(scene==='launch'){ $('hudObjective').textContent='Reach stable ascent';$('hudHint').textContent='SPACE ignition · ↑/↓ throttle · ←/→ tilt';$('controlSummary').textContent='LAUNCH: SPACE to ignite; ↑/↓ throttle. Keep 65–85% and angle within ±10°.'; }if(scene==='orbit'){ $('hudObjective').textContent='Time the lunar transfer burn';$('hudHint').textContent='Press SPACE only while the window is green';$('controlSummary').textContent='ORBIT: Watch the orbital indicator. Press SPACE only when the transfer window glows green.'; }if(scene==='landing'){ $('hudObjective').textContent='Touch down gently on the landing pad';$('hudHint').textContent='←/→ horizontal control · hold SPACE for thrust';$('controlSummary').textContent='LANDING: Use short SPACE thrust bursts to reduce vertical speed; steer toward the lit landing pad.'; }if(scene==='science'){ $('hudObjective').textContent='Collect 3 lunar samples';$('hudHint').textContent='←/→ walk · SPACE jump over craters';$('controlSummary').textContent='MOON: ←/→ to walk, SPACE to jump. Collect glowing samples and jump over craters.'; }if(scene==='entry'){ $('hudObjective').textContent='Hold the entry corridor';$('hudHint').textContent='←/→ correct capsule angle · SPACE deploy at green altitude';$('controlSummary').textContent='EARTH RETURN: keep angle near 0° with ←/→; deploy parachutes only when the indicator is green.'; }updateHud();}
function showOverlay(html){$('overlay').innerHTML=html;$('overlay').classList.remove('hidden');}
function showBriefing(){showOverlay('<div class="modal slim"><div class="eyebrow">Mission training</div><h2>Flight controls</h2><p>This is a real-time arcade mission. Fly the training craft, assemble your vehicle in the workshop, control the launch and lander, explore the lunar surface on foot, and steer your return capsule.</p><div class="message"><b>Keyboard:</b> WASD / arrow keys move; SPACE is phase-specific action. On touch screens use the on-screen directional pad and ACTION button.<br><br><b>Failure:</b> A debris collision, unsafe design, missed orbital burn, crash landing, sample-zone hazard, or incorrect entry control can end the mission immediately. Look at the HUD for the active objective.</div><div class="bar"><button class="primary" id="briefClose">Understood</button></div></div>');$('briefClose').onclick=()=>{if(game.scene==='menu')startTraining();else $('overlay').classList.add('hidden');};}
function startTraining(){game=freshGame();setScene('training');logLine('Flight training started. Navigate through three checkpoints.');showOverlay('<div class="modal slim"><div class="eyebrow">Phase 1 of 7 · Pilot training</div><h2>Training flight</h2><p>Steer the blue training craft through all three green navigation beacons. Avoid red debris. This introduces the movement and precision controls used later in the mission.</p><div class="message">Move with <b>W A S D</b> or the <b>arrow keys</b>. The game begins when you press Start training. A collision ends the mission.</div><div class="bar"><button class="primary" id="startTrainingNow">Start training →</button><button id="trainingHelp">Controls</button></div></div>');$('startTrainingNow').onclick=()=>{$('overlay').classList.add('hidden');tone(660,.09);};$('trainingHelp').onclick=showBriefing;updateHud();}
function optionById(type,id){return moduleOptions[type].find(item=>item.id===id)||moduleOptions[type][0];}
function designTotals(){const keys=['engine','lander','shield','power','life','comms','rover','spectrometer'];let mass=0,cost=0;for(const key of keys){const item=optionById(key,game.design[key]);mass+=item.mass;cost+=item.cost;}return {mass,cost,capacity:85,budget:100};}
function openDesign(){setScene('design');logLine('Training complete. Spacecraft assembly workshop opened.');const keys=[['engine','Main engine'],['lander','Lunar lander'],['shield','Heat shield'],['power','Power system'],['life','Life support'],['comms','Communications'],['rover','Science rover'],['spectrometer','Science payload']];const selectors=keys.map(([key,label])=>'<div class="module"><label for="module_'+key+'">'+label+'</label><select id="module_'+key+'">'+moduleOptions[key].map(item=>'<option value="'+item.id+'" '+(game.design[key]===item.id?'selected':'')+'>'+item.name+'</option>').join('')+'</select><div class="moddetail" id="detail_'+key+'"></div></div>').join('');showOverlay('<div class="modal"><div class="eyebrow">Phase 2 of 7 · Spacecraft assembly</div><h2>Build your lunar spacecraft</h2><p>Pick hardware and balance safety, mass, budget, power, science capability, and efficiency. The safe baseline is selected when you arrive. You can improve performance, but an unsafe critical subsystem or an overloaded vehicle ends the mission when you launch.</p><div class="design-grid">'+selectors+'</div><div class="designsummary"><div class="designstat"><strong id="buildMass">67 / 85</strong><small>Vehicle mass / capacity</small></div><div class="designstat"><strong id="buildCost">82 / 100</strong><small>Budget used / available</small></div><div class="designstat"><strong id="buildPower">100%</strong><small>Starting power reserve</small></div></div><div class="message" id="designMessage">Safe baseline configured. Check your trade-offs before launch.</div><div class="bar"><button class="primary" id="verifyBuild">Verify spacecraft and launch →</button><button id="resetBuild">Restore baseline</button></div></div>');for(const [key] of keys){$('module_'+key).onchange=()=>{game.design[key]=$('module_'+key).value;refreshDesignUi();};} $('verifyBuild').onclick=verifyDesign;$('resetBuild').onclick=()=>{game.design={engine:'balanced',lander:'two_stage',shield:'full',power:'solar',life:'redundant',comms:'highgain',rover:'none',spectrometer:'standard'};for(const [key] of keys)$('module_'+key).value=game.design[key];refreshDesignUi();};refreshDesignUi();}
function refreshDesignUi(){const keys=['engine','lander','shield','power','life','comms','rover','spectrometer'];const total=designTotals();$('buildMass').textContent=total.mass+' / '+total.capacity;$('buildCost').textContent=total.cost+' / '+total.budget;$('buildPower').textContent=game.design.power==='solar'?'100%':'40%';for(const key of keys){const item=optionById(key,game.design[key]);$('detail_'+key).textContent='Mass '+item.mass+' · Cost '+item.cost+' · '+item.desc;}const unsafe=keys.filter(key=>!optionById(key,game.design[key]).safe);const note=$('designMessage');note.className='message';if(unsafe.length){note.classList.add('bad');note.textContent='Critical configuration warning: '+unsafe.map(key=>key==='life'?'life support':key).join(', ')+' is not mission-safe. Select an approved safe system before launch.';}else if(total.mass>total.capacity||total.cost>total.budget){note.classList.add('bad');note.textContent='The vehicle exceeds its mass capacity or available budget. Reduce optional payload mass or choose a lighter, affordable safe configuration.';}else{note.classList.add('good');note.textContent='Vehicle is within budget and mass limits. All critical systems are selected. Review trade-offs, then verify the spacecraft.';}}
function verifyDesign(){const keys=['engine','lander','shield','power','life','comms','rover','spectrometer'];const total=designTotals();const unsafe=keys.filter(key=>!optionById(key,game.design[key]).safe);if(unsafe.length){criticalFailure('Unsafe spacecraft design','At least one critical system cannot support a crewed lunar landing and return. The spacecraft was approved despite an unresolved safety limitation.');return;}if(total.mass>total.capacity||total.cost>total.budget){criticalFailure('Spacecraft cannot launch','The design exceeds the launch mass capacity or mission budget. The mission was committed without bringing the vehicle within its constraints.');return;}game.mass=total.mass;game.budget=total.budget-total.cost;game.fuel=optionById('engine',game.design.engine).fuel;game.power=game.design.power==='solar'?100:40;game.score+=100;logLine('Spacecraft design verified: mass '+total.mass+'/'+total.capacity+', development cost '+total.cost+'/'+total.budget+'.');setScene('launch');showOverlay('<div class="modal slim"><div class="eyebrow">Phase 3 of 7 · Launch and ascent</div><h2>On the launch pad</h2><p>Vehicle checks are complete. At ignition, control throttle and attitude throughout ascent. Keep throttle in the marked green band and keep the rocket close to vertical.</p><div class="featuregrid"><div class="feature"><strong>65–85%</strong><span>Safe throttle band</span></div><div class="feature"><strong>±10°</strong><span>Safe pitch range</span></div><div class="feature"><strong>SPACE</strong><span>Ignition command</span></div></div><div class="bar"><button class="primary" id="igniteButton">Ignition — begin launch</button></div></div>');$('igniteButton').onclick=igniteLaunch;}
function igniteLaunch(){game.launch.ignited=true;$('overlay').classList.add('hidden');logLine('Main engines ignited. Ascent guidance active.');tone(110,.2,'sawtooth',.04);}
function criticalFailure(title,detail){if(game.failed||game.scene==='win')return;game.failed=true;game.integrity=0;game.report=title+': '+detail;setScene('fail');logLine('CRITICAL FAILURE: '+title);tone(90,.6,'sawtooth',.06);showOverlay('<div class="modal"><div class="eyebrow failure">Opposite ending · Mission terminated</div><h2>'+title+'</h2><p class="failure">'+detail+'</p><div class="message bad">Mission control has ended the mission. The happy ending is no longer possible on this flight. Review what happened and launch a new mission to try again.</div><div class="bar"><button class="primary" id="retryButton">Restart entire mission ↻</button><button id="failureLogButton">View flight log</button></div><div class="log hidden" id="failureLog"></div></div>');$('retryButton').onclick=startTraining;$('failureLogButton').onclick=()=>{$('failureLog').classList.toggle('hidden');$('failureLog').textContent=game.log.join('\n');};updateHud();}
function missionVictory(){setScene('win');game.score+=500;logLine('Earth recovery team confirmed crew safe. Mission complete.');tone(660,.15);setTimeout(()=>tone(880,.2),130);setTimeout(()=>tone(1100,.25),290);showOverlay('<div class="modal"><div class="eyebrow success">Successful ending · Crew recovered</div><h2>Welcome home, astronauts.</h2><p class="success">The spacecraft returned safely to Earth. Your crew completed flight training, designed a viable mission, launched successfully, reached lunar orbit, landed on the Moon, collected the required samples, and returned through the atmosphere for recovery.</p><div class="featuregrid"><div class="feature"><strong>100%</strong><span>Mission success</span></div><div class="feature"><strong>'+game.samples+'</strong><span>Lunar samples returned</span></div><div class="feature"><strong>'+game.score+'</strong><span>Mission score</span></div></div><div class="message good">Flight directors congratulate the crew. Science data and lunar samples have been secured. All crew members are home safe.</div><div class="bar"><button class="primary" id="flyAgain">Fly another mission ↻</button><button id="copyFlightLog">Copy flight log</button></div></div>');$('flyAgain').onclick=startTraining;$('copyFlightLog').onclick=async()=>{try{await navigator.clipboard.writeText(game.log.join('\n'));$('copyFlightLog').textContent='Flight log copied';}catch(e){$('copyFlightLog').textContent='Copy unavailable';}};updateHud();}
function moveToOrbit(){game.orbit={time:0,angle:0,ready:false,cycles:0};setScene('orbit');logLine('Earth orbit achieved. Awaiting lunar transfer window.');showOverlay('<div class="modal slim"><div class="eyebrow">Phase 4 of 7 · Lunar transfer</div><h2>Find the transfer window</h2><p>Your spacecraft is in Earth orbit. The timing indicator will rotate around the target. Press <b>SPACE</b> only when the indicator passes through the green transfer window. A premature or late burn will send the spacecraft off trajectory.</p><div class="message">Watch the orbit indicator on the screen. Wait for the green window; do not press the action key early.</div><div class="bar"><button class="primary" id="orbitReadyButton">Start orbital sequence</button></div></div>');$('orbitReadyButton').onclick=()=>{$('overlay').classList.add('hidden');game.orbit.time=0;};}
function beginLanding(){game.landing={x:500,y:95,vx:0,vy:.15,fuel:100,landed:false};setScene('landing');logLine('Lunar orbit achieved. Descent engine armed.');showOverlay('<div class="modal slim"><div class="eyebrow">Phase 5 of 7 · Moon landing</div><h2>Bring the lander down</h2><p>Gravity will accelerate the lander toward the surface. Steer left and right to center over the illuminated landing pad. Hold <b>SPACE</b> in short thrust bursts to lower your descent speed. The lander must touch down inside the pad with low horizontal and vertical speed.</p><div class="featuregrid"><div class="feature"><strong>SPACE</strong><span>Descent thrust</span></div><div class="feature"><strong>← / →</strong><span>Steer horizontally</span></div><div class="feature"><strong>Gentle</strong><span>Low-speed touchdown</span></div></div><div class="bar"><button class="primary" id="startDescent">Begin descent</button></div></div>');$('startDescent').onclick=()=>{$('overlay').classList.add('hidden');tone(180,.16,'sawtooth');};}
function beginScience(){game.science={x:90,y:FLOOR-18,vx:0,vy:0,camera:0,got:[],worldWidth:3000};setScene('science');logLine('Landing successful. EVA team is beginning surface science.');showOverlay('<div class="modal slim"><div class="eyebrow">Phase 6 of 7 · Lunar science</div><h2>Explore the Moon</h2><p>Guide the astronaut across the lunar surface and collect three glowing sample markers. Craters are hazards: jump over them with SPACE. Samples remain in your mission inventory once collected.</p><div class="message">Use <b>← / →</b> to walk and <b>SPACE</b> to jump. The lunar landscape scrolls as you explore.</div><div class="bar"><button class="primary" id="beginEVA">Start surface expedition</button></div></div>');$('beginEVA').onclick=()=>{$('overlay').classList.add('hidden');};}
function beginEntry(){game.entry={time:0,angle:0,deployed:false,stable:0};setScene('entry');logLine('Science objectives complete. Crew ascending for Earth return.');showOverlay('<div class="modal slim"><div class="eyebrow">Phase 7 of 7 · Return to Earth</div><h2>Navigate the atmosphere</h2><p>Keep the capsule in the green entry corridor near zero degrees. Atmospheric variation will push the capsule off attitude. Use <b>← / →</b> to correct the angle. When the parachute indicator becomes green, press <b>SPACE</b> to deploy.</p><div class="message">Too steep: dangerous heating. Too shallow: skip-out trajectory. Deploy parachutes outside the green zone and the recovery is lost.</div><div class="bar"><button class="primary" id="beginEntryButton">Begin atmospheric entry</button></div></div>');$('beginEntryButton').onclick=()=>{$('overlay').classList.add('hidden');};}
function updateHud(){if(!game)return;$('integrityStat').textContent=Math.round(game.integrity)+'%';$('crewStat').textContent=game.failed?'LOST':game.scene==='win'?'HOME SAFE':game.scene==='menu'?'READY':'ON MISSION';$('sampleStat').textContent=game.samples+' / 3';$('scoreStat').textContent=game.score;$('phaseBadge').textContent=game.scene.toUpperCase();$('topStatus').textContent=phaseTitles[game.scene]||'MISSION ACTIVE';$('fuelMeter').style.width=Math.max(0,game.fuel)+'%';$('fuelValue').textContent=Math.round(game.fuel)+'%';$('powerMeter').style.width=Math.max(0,game.power)+'%';$('powerValue').textContent=Math.round(game.power)+'%';$('hudTelemetry').textContent='INTEGRITY '+Math.round(game.integrity)+'%';$('missionLog').textContent=game.log.join('\n');const objectiveText={training:'Reach all 3 green checkpoints and avoid red debris.',design:'Choose a safe, affordable spacecraft within its mass capacity.',launch:'Keep throttle and attitude in safe limits until orbit.',orbit:'Press SPACE when the lunar transfer window is green.',landing:'Land inside the pad with low horizontal and vertical speed.',science:'Collect three glowing lunar samples and avoid crater hazards.',entry:'Keep the return capsule stable and deploy on the green signal.',win:'Mission accomplished. Crew recovered safely.',fail:'The mission ended after a critical mistake.'};const done=phases.indexOf(game.scene);$('objectiveList').innerHTML=phases.map((phase,index)=>'<div class="objectiveline"><span class="dot">'+(index+1)+'</span><span style="color:'+(index<done||game.scene==='win'?'#aaf2d0':phase===game.scene?'#66e7ff':'#a7bad6')+'">'+phaseTitles[phase]+(phase===game.scene?' · CURRENT':'')+'</span></div>').join('')+'<div style="font-size:10px;color:#b6c8e1;line-height:1.5;margin-top:8px">'+(objectiveText[game.scene]||'Prepare your mission.')+'</div>';}
function loadAtlas(){fetch('/api/atlas').then(response=>response.json()).then(data=>{worldAtlas=data.stars||[];}).catch(()=>{worldAtlas=Array.from({length:240},(_,i)=>({x:(i*97)%3200,y:(i*53)%430,brightness:1+(i%3)}));});}
function keyName(event){if(event.code==='Space')return 'Space';if(event.key===' ')return 'Space';return event.key.length===1?event.key.toLowerCase():event.key;}
window.addEventListener('keydown',event=>{const key=keyName(event);if(['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','Space',' '].includes(event.code)||['ArrowUp','ArrowDown','ArrowLeft','ArrowRight'].includes(event.key))event.preventDefault();if(['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','w','a','s','d','W','A','S','D','Space'].includes(key)){held.add(key);if(key==='Space'&&game.scene==='launch'&&!game.launch.ignited){igniteLaunch();}else if(key==='Space'&&game.scene==='orbit'&&$('overlay').classList.contains('hidden'))attemptOrbitBurn();else if(key==='Space'&&game.scene==='entry'&&$('overlay').classList.contains('hidden'))attemptParachute();}});
window.addEventListener('keyup',event=>{held.delete(keyName(event));});
window.addEventListener('blur',()=>held.clear());
$('beginButton').onclick=startTraining;
$('briefButton').onclick=showBriefing;
$('restartTop').onclick=()=>{if(game.scene==='menu')startTraining();else showOverlay('<div class="modal slim"><div class="eyebrow">Restart mission?</div><h2>Reset this flight</h2><p>Your current mission progress will be lost. Start over from flight training?</p><div class="bar"><button class="primary" id="confirmRestart">Restart mission</button><button id="cancelRestart">Keep flying</button></div></div>');if($('confirmRestart'))$('confirmRestart').onclick=startTraining;if($('cancelRestart'))$('cancelRestart').onclick=()=>$('overlay').classList.add('hidden');};
$('soundButton').onclick=()=>{soundEnabled=!soundEnabled;$('soundButton').textContent='Sound: '+(soundEnabled?'on':'off');if(soundEnabled)tone(660,.08);};
$('pauseButton').onclick=()=>{if(['menu','win','fail','design'].includes(game.scene))return;paused=!paused;$('pauseButton').textContent=paused?'Resume':'Pause';if(paused)showOverlay('<div class="modal slim"><div class="eyebrow">Flight paused</div><h2>Mission on hold</h2><p>Your spacecraft is paused. Resume when ready.</p><div class="bar"><button class="primary" id="resumeButton">Resume flight</button><button id="pauseRestart">Restart mission</button></div></div>');else $('overlay').classList.add('hidden');$('resumeButton')&&($('resumeButton').onclick=()=>{paused=false;$('overlay').classList.add('hidden');$('pauseButton').textContent='Pause';});$('pauseRestart')&&($('pauseRestart').onclick=startTraining);};
document.querySelectorAll('[data-key]').forEach(button=>{const key=button.dataset.key;const down=event=>{event.preventDefault();held.add(key==='Space'?'Space':key);if(key==='Space'&&game.scene==='launch'&&!game.launch.ignited)igniteLaunch();if(key==='Space'&&game.scene==='orbit'&&$('overlay').classList.contains('hidden'))attemptOrbitBurn();if(key==='Space'&&game.scene==='entry'&&$('overlay').classList.contains('hidden'))attemptParachute();};const up=event=>{event.preventDefault();held.delete(key==='Space'?'Space':key);};button.addEventListener('pointerdown',down);button.addEventListener('pointerup',up);button.addEventListener('pointercancel',up);button.addEventListener('pointerleave',up);});
function pressed(...names){return names.some(name=>held.has(name));}
function attemptOrbitBurn(){if(game.scene!=='orbit'||!$('overlay').classList.contains('hidden'))return;if(game.orbit.ready){game.score+=100;game.fuel=Math.max(0,game.fuel-12);logLine('Lunar transfer burn executed inside the verified window.');tone(520,.14);beginLanding();}else{criticalFailure('Missed lunar transfer window','The engine was commanded outside the planned burn window. The spacecraft missed its safe lunar trajectory.');}}
function attemptParachute(){if(game.scene!=='entry'||!$('overlay').classList.contains('hidden')||game.entry.deployed)return;const time=game.entry.time;if(time>=8.5&&time<=12.5&&Math.abs(game.entry.angle)<=4){game.entry.deployed=true;game.score+=150;logLine('Parachutes deployed inside the entry corridor. Recovery systems active.');tone(740,.15);}else{criticalFailure('Unsafe parachute deployment','The recovery system was deployed outside the verified altitude and attitude window. Safe landing could not be assured.');}}
function updateGame(dt){if(paused||!game||['menu','design','win','fail'].includes(game.scene)||!$('overlay').classList.contains('hidden'))return;const f=dt*60;game.time+=dt;game.elapsed+=dt;if(game.scene==='training')updateTraining(f,dt);if(game.scene==='launch')updateLaunch(f,dt);if(game.scene==='orbit')updateOrbit(f,dt);if(game.scene==='landing')updateLanding(f,dt);if(game.scene==='science')updateScience(f,dt);if(game.scene==='entry')updateEntry(f,dt);}
function updateTraining(f,dt){const s=game.training;const speed=s.speed;let dx=(pressed('ArrowRight','d','D')?1:0)-(pressed('ArrowLeft','a','A')?1:0);let dy=(pressed('ArrowDown','s','S')?1:0)-(pressed('ArrowUp','w','W')?1:0);if(dx&&dy){dx*=.707;dy*=.707;}s.x+=dx*speed*f;s.y+=dy*speed*f;s.x=Math.max(28,Math.min(WIDTH-28,s.x));s.y=Math.max(48,Math.min(HEIGHT-28,s.y));for(const hazard of s.hazards){hazard.cx=hazard.x+Math.sin(game.time*hazard.speed+hazard.phase)*72;hazard.cy=hazard.y+Math.cos(game.time*hazard.speed*.8+hazard.phase)*35;const distance=Math.hypot(s.x-hazard.cx,s.y-hazard.cy);if(distance<hazard.r+11){criticalFailure('Training craft collision','The training vehicle struck a debris hazard. The simulation treats a collision as a critical mission-ending mistake.');return;}}const target=s.targets[s.target];if(target&&Math.hypot(s.x-target.x,s.y-target.y)<27){s.target++;game.score+=25;tone(760,.09);logLine('Navigation checkpoint '+s.target+'/3 confirmed.');if(s.target===s.targets.length){game.score+=50;openDesign();return;}}updateHud();}
function updateLaunch(f,dt){const s=game.launch;if(!s.ignited)return;const throttleUp=pressed('ArrowUp','w','W');const throttleDown=pressed('ArrowDown','s','S');const tiltLeft=pressed('ArrowLeft','a','A');const tiltRight=pressed('ArrowRight','d','D');if(throttleUp)s.throttle+=.75*f;if(throttleDown)s.throttle-=.75*f;if(tiltLeft)s.angle-=.32*f;if(tiltRight)s.angle+=.32*f;s.throttle=Math.max(0,Math.min(100,s.throttle));s.angle=Math.max(-45,Math.min(45,s.angle));if(s.throttle<65||s.throttle>85||Math.abs(s.angle)>10)s.outOfBand+=dt;else s.outOfBand=Math.max(0,s.outOfBand-dt*.4);if(s.throttle<32||s.throttle>96||Math.abs(s.angle)>24||s.outOfBand>1.65){criticalFailure('Launch guidance lost','Throttle or rocket attitude remained outside safe flight limits. The vehicle could not recover a stable ascent.');return;}s.altitude+=Math.max(0,(s.throttle-42)/33)*.52*f*Math.max(.2,Math.cos(s.angle*Math.PI/180));game.fuel=Math.max(0,game.fuel-.025*f*(s.throttle/75));if(s.altitude>=100){s.altitude=100;game.score+=100;moveToOrbit();return;}updateHud();}
function updateOrbit(f,dt){const s=game.orbit;s.time+=dt;s.angle+=dt*1.22;s.ready=Math.sin(s.angle)>Math.cos(.58);if(s.ready&& !s.wasReady){tone(680,.035,'sine',.012);}s.wasReady=s.ready;s.cycles=Math.floor(s.angle/(Math.PI*2));if(s.time>42){criticalFailure('Transfer window expired','The crew did not execute the lunar transfer within the simulated mission window.');return;}updateHud();}
function updateLanding(f,dt){const s=game.landing;const left=pressed('ArrowLeft','a','A');const right=pressed('ArrowRight','d','D');const thrust=pressed('Space','ArrowUp','w','W');s.vx+=(right?1:0)*.045*f;s.vx-=(left?1:0)*.045*f;s.vx*=Math.pow(.985,f);s.vx=Math.max(-2.6,Math.min(2.6,s.vx));s.vy+=.035*f;if(thrust&&s.fuel>0){s.vy-=.071*f;s.fuel=Math.max(0,s.fuel-.12*f);game.fuel=s.fuel;}s.vy=Math.max(-1.5,Math.min(6.2,s.vy));s.x+=s.vx*f;s.y+=s.vy*f;s.x=Math.max(25,Math.min(975,s.x));if(s.y>=FLOOR-13){const pad=s.x>=430&&s.x<=570;const vertical=Math.abs(s.vy);const horizontal=Math.abs(s.vx);if(pad&&vertical<=1.35&&horizontal<=1.25&&s.fuel>2){s.y=FLOOR-13;s.landed=true;game.integrity=100;game.fuel=s.fuel;game.score+=150;game.samples=0;tone(880,.2);beginScience();return;}criticalFailure('Lunar landing crash','The lander missed the safe pad or touched down above the permitted speed. A successful surface landing was not possible.');return;}if(s.x<28||s.x>972){criticalFailure('Landing guidance lost','The lander drifted beyond its controlled landing corridor.');return;}if(s.fuel<=0&&s.vy>2.5){criticalFailure('Descent propellant exhausted','The lander ran out of braking propellant before a safe touchdown.');return;}updateHud();}
const sampleLocations=[{id:'sample-a',x:430,y:FLOOR-20,label:'Basalt sample'},{id:'sample-b',x:1280,y:FLOOR-20,label:'Lunar soil'},{id:'sample-c',x:2180,y:FLOOR-20,label:'Highland fragment'}];
const craterLocations=[{x:790,w:48},{x:1575,w:54},{x:2460,w:60}];
function updateScience(f,dt){const s=game.science;const left=pressed('ArrowLeft','a','A');const right=pressed('ArrowRight','d','D');const jump=pressed('Space','ArrowUp','w','W');if(left)s.vx-=.08*f;if(right)s.vx+=.08*f;s.vx*=Math.pow(.86,f);s.vx=Math.max(-3.3,Math.min(3.3,s.vx));if(jump&&Math.abs(s.vy)<.1&&s.y>=FLOOR-18){s.vy=-6.2;tone(360,.045);}s.vy+=.28*f;s.x+=s.vx*f;s.y+=s.vy*f;s.x=Math.max(20,Math.min(s.worldWidth-20,s.x));if(s.y>FLOOR-18){s.y=FLOOR-18;s.vy=0;}s.camera=Math.max(0,Math.min(s.worldWidth-WIDTH,s.x-WIDTH*.36));for(const crater of craterLocations){if(Math.abs(s.x-crater.x)<crater.w*.45+9&&s.y>=FLOOR-27){criticalFailure('Astronaut fell into a lunar crater','The EVA route crossed a deep crater without jumping over the hazard. The crew member could not continue the mission.');return;}}for(const sample of sampleLocations){if(!s.got.includes(sample.id)&&Math.hypot(s.x-sample.x,s.y-sample.y)<35){s.got.push(sample.id);game.samples=s.got.length;game.score+=75;tone(940,.1);logLine(sample.label+' secured. '+game.samples+'/3 samples aboard.');if(game.samples===3){beginEntry();return;}}}updateHud();}
function updateEntry(f,dt){const s=game.entry;s.time+=dt;const steer=(pressed('ArrowRight','d','D')?1:0)-(pressed('ArrowLeft','a','A')?1:0);const disturbance=Math.sin(s.time*2.2)*.09+Math.sin(s.time*.71)*.04;s.angle+=steer*.34*f+disturbance*f*.22;s.angle*=Math.pow(.986,f);s.angle=Math.max(-14,Math.min(14,s.angle));if(Math.abs(s.angle)>6.3)s.stable+=dt;else s.stable=Math.max(0,s.stable-dt*.5);if(s.stable>.95){criticalFailure('Atmospheric entry corridor lost','Capsule attitude left the safe entry corridor for too long. The vehicle overheated or skipped away from the atmosphere.');return;}if(s.deployed&&s.time>15){missionVictory();return;}if(!s.deployed&&s.time>19){criticalFailure('Recovery altitude passed','The capsule passed the parachute deployment window before recovery systems were activated.');return;}updateHud();}
function drawBackground(offset=0,moon=false){const gradient=ctx.createLinearGradient(0,0,0,HEIGHT);gradient.addColorStop(0,'#050917');gradient.addColorStop(.55,'#101d35');gradient.addColorStop(1,'#0c1221');ctx.fillStyle=gradient;ctx.fillRect(0,0,WIDTH,HEIGHT);for(const star of worldAtlas){let x=((star.x-offset*.07)%3200+3200)%3200;if(x<WIDTH&&star.y<HEIGHT*.82){ctx.fillStyle=star.color||'#c8e5ff';ctx.globalAlpha=.35+(star.brightness||1)*.18;const size=star.brightness>=3?2.5:star.brightness>=2?1.7:1;ctx.fillRect(Math.round(x),Math.round(star.y),size,size);if(star.brightness>=4){ctx.globalAlpha=.2;ctx.fillRect(x-3,star.y+1,7,1);ctx.fillRect(x+1,star.y-3,1,7);}}}ctx.globalAlpha=1;if(moon){ctx.save();ctx.shadowColor='#91bfe8';ctx.shadowBlur=30;const rg=ctx.createRadialGradient(735,177,20,735,177,122);rg.addColorStop(0,'#ecf2f5');rg.addColorStop(.4,'#a8bbd4');rg.addColorStop(.85,'#5d7192');rg.addColorStop(1,'#263651');ctx.fillStyle=rg;ctx.beginPath();ctx.arc(735,177,119,0,Math.PI*2);ctx.fill();ctx.restore();for(let i=0;i<26;i++){const x=680+(i*47)%105;const y=115+(i*31)%125;ctx.fillStyle=i%2?'#6d809d':'#d2dce8';ctx.globalAlpha=.18;ctx.beginPath();ctx.arc(x,y,2+(i%4),0,Math.PI*2);ctx.fill();}ctx.globalAlpha=1;}}
function drawText(text,x,y,size=16,color='#edf6ff',align='left'){ctx.font='bold '+size+'px ui-monospace,Consolas,monospace';ctx.fillStyle=color;ctx.textAlign=align;ctx.fillText(text,x,y);ctx.textAlign='left';}
function drawPixelShip(x,y,scale=1,angle=0,color='#68e9ff',flame=false){ctx.save();ctx.translate(x,y);ctx.rotate(angle*Math.PI/180);ctx.scale(scale,scale);ctx.fillStyle='#dbe7f8';ctx.fillRect(-7,-18,14,25);ctx.fillStyle='#8296b8';ctx.fillRect(-12,-10,5,18);ctx.fillRect(7,-10,5,18);ctx.fillStyle='#e9f3ff';ctx.fillRect(-4,-25,8,10);ctx.fillStyle='#40cfff';ctx.fillRect(-3,-22,6,5);ctx.fillStyle='#ffbb6c';ctx.fillRect(-4,7,8,8);if(flame){ctx.fillStyle='#ff5b62';ctx.fillRect(-4,14,8,Math.floor(5+Math.random()*12));ctx.fillStyle='#ffde7b';ctx.fillRect(-2,14,4,Math.floor(3+Math.random()*9));}ctx.restore();}
function drawRocket(){const s=game.launch;ctx.fillStyle='#142d4b';ctx.fillRect(0,465,WIDTH,97);for(let i=0;i<7;i++){ctx.fillStyle='#264d73';ctx.fillRect(i*155+18,495,88,40);}ctx.fillStyle='#192c43';ctx.fillRect(455,435,90,30);ctx.fillRect(475,388,50,50);const y=415-s.altitude*3.45;ctx.save();ctx.translate(500,y);ctx.rotate(s.angle*Math.PI/180);ctx.fillStyle='#bfcde1';ctx.fillRect(-17,-77,34,110);ctx.fillStyle='#f4f7ff';ctx.beginPath();ctx.moveTo(-17,-77);ctx.lineTo(0,-109);ctx.lineTo(17,-77);ctx.fill();ctx.fillStyle='#65e5ff';ctx.fillRect(-8,-58,16,20);ctx.fillStyle='#da6279';ctx.fillRect(-26,10,9,27);ctx.fillRect(17,10,9,27);if(s.ignited){ctx.fillStyle='#ff9d55';ctx.fillRect(-9,33,18,Math.random()*22+9);ctx.fillStyle='#fff0a4';ctx.fillRect(-4,34,8,Math.random()*13+7);}ctx.restore();ctx.fillStyle='#081426';ctx.fillRect(35,24,185,82);ctx.strokeStyle='#3e5c7b';ctx.strokeRect(35,24,185,82);drawText('ASCENT',49,47,12,'#72e9ff');drawText('ALT '+Math.floor(s.altitude)+'%',49,68,14);drawText('THR '+Math.floor(s.throttle)+'%',49,89,13,s.throttle>=65&&s.throttle<=85?'#80f0b3':'#ff7088');ctx.fillStyle='#263750';ctx.fillRect(49,95,150,5);ctx.fillStyle='#76edb4';ctx.fillRect(49+150*.65,95,150*.2,5);ctx.fillStyle='#55dfff';ctx.fillRect(49,95,150*s.altitude/100,5);ctx.strokeStyle='#6b829e';ctx.strokeRect(425,115,150,250);ctx.strokeStyle='#70e8ff';ctx.beginPath();ctx.moveTo(500,119);ctx.lineTo(500,361);ctx.stroke();ctx.strokeStyle='#72efb1';ctx.beginPath();ctx.moveTo(450,240);ctx.lineTo(550,240);ctx.stroke();ctx.fillStyle='#091427';ctx.fillRect(770,24,190,95);drawText('ATTITUDE',785,47,11,'#72e9ff');drawText((s.angle>0?'+':'')+s.angle.toFixed(1)+'°',785,77,22,Math.abs(s.angle)<=10?'#78f0b1':'#ff7188');drawText('TARGET 0°',785,101,11,'#a8bbd5');}
function drawTraining(){drawBackground(game.camera,false);const s=game.training;ctx.strokeStyle='#233b5e';ctx.lineWidth=1;for(let x=0;x<WIDTH;x+=50){ctx.beginPath();ctx.moveTo(x,35);ctx.lineTo(x,HEIGHT);ctx.stroke();}for(let y=50;y<HEIGHT;y+=50){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(WIDTH,y);ctx.stroke();}const target=s.targets[s.target];if(target){const pulse=6+Math.sin(game.time*5)*3;ctx.strokeStyle='#68ffb7';ctx.lineWidth=3;ctx.beginPath();ctx.arc(target.x,target.y,20+pulse,0,Math.PI*2);ctx.stroke();ctx.globalAlpha=.4;ctx.fillStyle='#45ffc1';ctx.beginPath();ctx.arc(target.x,target.y,30+pulse,0,Math.PI*2);ctx.fill();ctx.globalAlpha=1;drawText('CHECKPOINT '+(s.target+1),target.x,target.y-34,11,'#82ffbe','center');}s.hazards.forEach(h=>{const x=h.cx===undefined?h.x:h.cx;const y=h.cy===undefined?h.y:h.cy;ctx.fillStyle='#482134';ctx.beginPath();ctx.arc(x,y,h.r+5,0,Math.PI*2);ctx.fill();ctx.fillStyle='#ff657b';ctx.beginPath();ctx.arc(x,y,h.r,0,Math.PI*2);ctx.fill();ctx.fillStyle='#9c304d';ctx.fillRect(x-h.r*.7,y-h.r*.3,h.r*.9,h.r*.4);});drawPixelShip(s.x,s.y,1,0,'#68e9ff',false);ctx.fillStyle='#071325';ctx.fillRect(18,18,245,53);ctx.strokeStyle='#385272';ctx.strokeRect(18,18,245,53);drawText('FLIGHT TRAINING',31,39,12,'#68e7ff');drawText('BEACONS '+s.target+'/3',31,59,14);}
function drawOrbit(){drawBackground(game.orbit.time*70,true);const s=game.orbit;ctx.save();ctx.translate(500,330);ctx.strokeStyle='#7bb0dd';ctx.lineWidth=2;ctx.beginPath();ctx.ellipse(0,0,245,85,-.25,0,Math.PI*2);ctx.stroke();ctx.strokeStyle=s.ready?'#72ffb6':'#526a86';ctx.lineWidth=s.ready?5:2;ctx.beginPath();ctx.arc(0,0,245,s.angle-.34,s.angle+.34);ctx.stroke();const sx=Math.cos(s.angle)*245;const sy=Math.sin(s.angle)*85;drawPixelShip(sx,sy,.85,-s.angle*30,'#77e9ff',false);ctx.restore();ctx.fillStyle='#09162a';ctx.fillRect(20,20,250,102);ctx.strokeStyle='#344d6e';ctx.strokeRect(20,20,250,102);drawText('LUNAR TRANSFER',35,44,12,'#70eaff');drawText(s.ready?'BURN WINDOW OPEN':'WAIT FOR GREEN',35,70,15,s.ready?'#78f0b1':'#ffd874');drawText('PRESS SPACE TO COMMIT',35,96,10,'#a9bfdc');ctx.save();ctx.translate(500,330);ctx.strokeStyle='#b9c9e5';ctx.lineWidth=2;ctx.beginPath();ctx.arc(0,0,160,0,Math.PI*2);ctx.stroke();ctx.rotate(s.angle);ctx.strokeStyle=s.ready?'#7affbc':'#ffcf72';ctx.lineWidth=5;ctx.beginPath();ctx.arc(0,0,160,-.35,.35);ctx.stroke();ctx.restore();}
function drawLanding(){drawBackground(game.time*15,true);const s=game.landing;ctx.fillStyle='#aebdd1';ctx.beginPath();ctx.moveTo(0,485);for(let x=0;x<=WIDTH;x+=25){ctx.lineTo(x,480+Math.sin(x*.016)*5+Math.sin(x*.043)*3);}ctx.lineTo(WIDTH,HEIGHT);ctx.lineTo(0,HEIGHT);ctx.closePath();ctx.fill();ctx.fillStyle='#8496ae';for(let i=0;i<90;i++){const x=(i*137)%WIDTH;const y=488+(i*17)%68;ctx.fillRect(x,y,2+(i%4),1+(i%2));}ctx.fillStyle='#081426';ctx.fillRect(418,468,164,18);ctx.strokeStyle='#71ffb8';ctx.lineWidth=2;ctx.strokeRect(432,467,136,18);ctx.fillStyle='#163b36';ctx.fillRect(439,473,122,5);ctx.fillStyle='#70fbb4';ctx.fillRect(494,461,12,7);ctx.fillStyle='#09162a';ctx.fillRect(20,20,235,95);ctx.strokeStyle='#385271';ctx.strokeRect(20,20,235,95);drawText('DESCENT TELEMETRY',34,42,11,'#6de7ff');drawText('V-SPEED '+s.vy.toFixed(2),34,66,14,Math.abs(s.vy)<1.35?'#79f0b1':'#ffcf72');drawText('H-SPEED '+s.vx.toFixed(2),34,89,13,Math.abs(s.vx)<1.25?'#79f0b1':'#ffcf72');ctx.fillStyle='#09162a';ctx.fillRect(790,20,185,81);drawText('BRAKING FUEL',805,42,10,'#71e7ff');ctx.fillStyle='#273951';ctx.fillRect(805,54,150,9);ctx.fillStyle=s.fuel<25?'#ff7088':'#75ecb3';ctx.fillRect(805,54,150*s.fuel/100,9);drawText(Math.round(s.fuel)+'%',805,82,14);drawPixelShip(s.x,s.y,1.2,0,'#e1ebfa',pressed('Space','ArrowUp','w','W'));if(pressed('Space','ArrowUp','w','W')){ctx.fillStyle='#ffb766';ctx.fillRect(s.x-7,s.y+24,14,Math.random()*20+10);ctx.fillStyle='#fff1a0';ctx.fillRect(s.x-3,s.y+24,6,Math.random()*12+7);}drawText('LANDING PAD',500,452,11,'#81ffc0','center');}
function drawMoonGround(offset){ctx.fillStyle='#0a1220';ctx.fillRect(0,0,WIDTH,HEIGHT);for(const star of worldAtlas){const x=((star.x-offset*.03)%3200+3200)%3200;if(x<WIDTH&&star.y<270){ctx.fillStyle=star.color||'#c8e5ff';ctx.globalAlpha=.25+(star.brightness||1)*.12;ctx.fillRect(x,star.y,star.brightness>=3?2:1,star.brightness>=3?2:1);}}ctx.globalAlpha=1;ctx.fillStyle='#8793a7';ctx.beginPath();ctx.moveTo(0,FLOOR);for(let x=0;x<=WIDTH;x+=10){const wx=x+offset;let height=0;for(const crater of craterLocations){const d=Math.abs(wx-crater.x);if(d<crater.w/2)height=Math.max(height,Math.sqrt(Math.max(0,1-(d/(crater.w/2))**2))*13);}ctx.lineTo(x,FLOOR-height);}ctx.lineTo(WIDTH,HEIGHT);ctx.lineTo(0,HEIGHT);ctx.closePath();ctx.fill();ctx.fillStyle='#aeb8c8';for(let i=0;i<130;i++){const wx=(i*89+13)%3100;const x=wx-offset;if(x>=0&&x<WIDTH){const y=FLOOR+3+(i*23)%66;ctx.globalAlpha=.18+(i%4)*.1;ctx.fillRect(x,y,1+(i%3),1);}}ctx.globalAlpha=1;for(const crater of craterLocations){const x=crater.x-offset;if(x>-crater.w&&x<WIDTH+crater.w){ctx.fillStyle='#424e64';ctx.beginPath();ctx.ellipse(x,FLOOR-1,crater.w/2,14,0,Math.PI,Math.PI*2);ctx.fill();ctx.strokeStyle='#c1cad9';ctx.lineWidth=2;ctx.beginPath();ctx.ellipse(x,FLOOR-1,crater.w/2,14,0,Math.PI,Math.PI*2);ctx.stroke();ctx.fillStyle='#060b15';ctx.beginPath();ctx.ellipse(x,FLOOR,crater.w*.35,7,0,0,Math.PI*2);ctx.fill();}}for(const sample of sampleLocations){const x=sample.x-offset;if(x>-25&&x<WIDTH+25){const bob=Math.sin(game.time*3+sample.x)*3;ctx.fillStyle='#e9c772';ctx.fillRect(x-8,FLOOR-30+bob,16,11);ctx.fillStyle='#fff3ad';ctx.fillRect(x-4,FLOOR-35+bob,8,7);ctx.strokeStyle='#ffe99b';ctx.globalAlpha=.4;ctx.beginPath();ctx.arc(x,FLOOR-20+bob,18+Math.sin(game.time*4)*3,0,Math.PI*2);ctx.stroke();ctx.globalAlpha=1;}}for(let i=0;i<18;i++){const x=((i*173+83-offset*.5)%WIDTH+WIDTH)%WIDTH;ctx.fillStyle=i%2?'#5f6d81':'#7a879b';ctx.fillRect(x,FLOOR-8-(i%3)*4,5+(i%5),5+(i%3));}}
function drawAstronaut(x,y){ctx.save();ctx.translate(x,y);ctx.fillStyle='#e1eaf6';ctx.fillRect(-7,-18,14,16);ctx.fillRect(-9,-4,7,12);ctx.fillRect(2,-4,7,12);ctx.fillStyle='#d0dbeb';ctx.fillRect(-10,-22,20,5);ctx.fillStyle='#70e7ff';ctx.fillRect(-5,-24,10,9);ctx.fillStyle='#b9c8dc';ctx.fillRect(-11,-2,5,14);ctx.fillRect(6,-2,5,14);ctx.fillStyle='#8f9fb7';ctx.fillRect(-10,9,7,4);ctx.fillRect(3,9,7,4);ctx.fillStyle='#fff';ctx.fillRect(-3,-20,6,3);ctx.restore();}
function drawScience(){const s=game.science;drawMoonGround(s.camera);const x=s.x-s.camera;drawAstronaut(x,s.y);ctx.fillStyle='#081426';ctx.fillRect(20,18,210,70);ctx.strokeStyle='#395372';ctx.strokeRect(20,18,210,70);drawText('LUNAR EVA',34,40,11,'#70eaff');drawText('SAMPLES '+game.samples+'/3',34,63,14,game.samples===3?'#78f0b1':'#eef6ff');drawText('WALKING',34,80,9,'#a7bad6');drawText('SPACE: JUMP',980,35,10,'#ffd874','right');}
function drawEntry(){drawBackground(game.time*110,false);const s=game.entry;const reentry=1-Math.min(1,s.time/15);ctx.save();ctx.translate(500,270);ctx.rotate(s.angle*Math.PI/180);ctx.fillStyle='#d1dbea';ctx.beginPath();ctx.moveTo(-36,-18);ctx.lineTo(0,-52);ctx.lineTo(36,-18);ctx.lineTo(29,23);ctx.lineTo(-29,23);ctx.closePath();ctx.fill();ctx.fillStyle='#8fb3d9';ctx.fillRect(-18,-12,36,17);ctx.fillStyle='#7b899e';ctx.fillRect(-25,21,50,10);ctx.fillStyle=s.deployed?'#d8e8ff':'#ff825a';ctx.globalAlpha=.45+Math.random()*.35;ctx.beginPath();ctx.moveTo(-29,24);ctx.lineTo(-55,68);ctx.lineTo(-17,48);ctx.lineTo(0,67);ctx.lineTo(16,48);ctx.lineTo(55,68);ctx.lineTo(29,24);ctx.closePath();ctx.fill();ctx.globalAlpha=1;ctx.restore();ctx.fillStyle='#091427';ctx.fillRect(20,20,250,120);ctx.strokeStyle='#405673';ctx.strokeRect(20,20,250,120);drawText('ATMOSPHERIC ENTRY',34,43,11,'#71e7ff');drawText('ATTITUDE '+(s.angle>0?'+':'')+s.angle.toFixed(1)+'°',34,69,14,Math.abs(s.angle)<=4?'#78f0b1':'#ffcf72');drawText('ALTITUDE '+Math.max(0,Math.round((1-s.time/18)*100))+'%',34,94,12);drawText(s.deployed?'PARACHUTES OPEN':'PARACHUTE WINDOW '+(s.time>=8.5&&s.time<=12.5?'OPEN':'CLOSED'),34,119,10,s.deployed?'#78f0b1':s.time>=8.5&&s.time<=12.5?'#78f0b1':'#ffd874');ctx.fillStyle='#243650';ctx.fillRect(34,125,205,5);ctx.fillStyle='#72f0b4';ctx.fillRect(34+205*.43,125,205*.22,5);ctx.fillStyle='#081426';ctx.fillRect(750,20,225,72);drawText('ENTRY CORRIDOR',765,43,10,'#7defff');ctx.strokeStyle='#7af0b5';ctx.strokeRect(790,54,145,20);ctx.fillStyle='#2c906b';ctx.fillRect(790,54,145,20);ctx.fillStyle='#ffcf73';ctx.fillRect(860+s.angle*4,50,5,28);drawText('KEEP IT CENTERED',765,84,9,'#a8bad5');}
function drawMenu(){drawBackground(game.time*6,true);ctx.fillStyle='#050b18b8';ctx.fillRect(0,0,WIDTH,HEIGHT);ctx.save();ctx.translate(505,308);ctx.rotate(-.08);ctx.strokeStyle='#3b86bd';ctx.lineWidth=2;ctx.beginPath();ctx.ellipse(0,0,300,88,0,0,Math.PI*2);ctx.stroke();ctx.restore();drawPixelShip(500,240,1.8,-8,'#9aeeff',false);drawText('LUNAR PATH',500,375,31,'#edf7ff','center');drawText('SPACE MISSION DESIGN GAME',500,408,13,'#69e7ff','center');drawText('TRAIN · BUILD · LAUNCH · LAND · EXPLORE · RETURN',500,444,10,'#b7cbe4','center');}
function drawDesignBackdrop(){drawBackground(game.time*10,true);ctx.fillStyle='#0a1324';ctx.fillRect(0,378,WIDTH,184);ctx.strokeStyle='#2e4564';for(let x=0;x<WIDTH;x+=40){ctx.beginPath();ctx.moveTo(x,378);ctx.lineTo(x,562);ctx.stroke();}for(let y=390;y<562;y+=30){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(WIDTH,y);ctx.stroke();}ctx.fillStyle='#b7cbe0';ctx.fillRect(470,240,60,128);ctx.fillStyle='#ecf4ff';ctx.beginPath();ctx.moveTo(470,240);ctx.lineTo(500,195);ctx.lineTo(530,240);ctx.fill();ctx.fillStyle='#5c7797';ctx.fillRect(438,264,32,74);ctx.fillRect(530,264,32,74);ctx.fillStyle='#61e4fa';ctx.fillRect(479,260,42,35);ctx.fillStyle='#ffb76b';ctx.fillRect(487,368,26,8);drawText('ASSEMBLY WORKSHOP',36,45,12,'#6ce6ff');drawText('COMPONENT CHOICES ARE SHOWN IN THE WORKSHOP PANEL',36,68,10,'#a9bfdc');}
function render(){ctx.clearRect(0,0,WIDTH,HEIGHT);if(game.scene==='menu')drawMenu();else if(game.scene==='training')drawTraining();else if(game.scene==='design')drawDesignBackdrop();else if(game.scene==='launch')drawRocket();else if(game.scene==='orbit')drawOrbit();else if(game.scene==='landing')drawLanding();else if(game.scene==='science')drawScience();else if(game.scene==='entry')drawEntry();else if(game.scene==='win'){drawBackground(game.time*4,true);drawText('EARTH RECOVERY CONFIRMED',WIDTH/2,HEIGHT/2,24,'#8ff4bd','center');}else if(game.scene==='fail'){drawBackground(game.time*20,false);ctx.fillStyle='#5e1728';ctx.globalAlpha=.35;ctx.fillRect(0,0,WIDTH,HEIGHT);ctx.globalAlpha=1;drawText('MISSION TERMINATED',WIDTH/2,HEIGHT/2,25,'#ff7e91','center');}if(game.scene==='orbit'){const s=game.orbit;const c=s.ready?'#77f4af':'#ffd475';ctx.strokeStyle=c;ctx.lineWidth=3;ctx.beginPath();ctx.arc(500,330,176,0,Math.PI*2);ctx.stroke();const x=500+Math.cos(s.angle)*176;const y=330+Math.sin(s.angle)*176;ctx.fillStyle=c;ctx.beginPath();ctx.arc(x,y,8,0,Math.PI*2);ctx.fill();}if(game.scene==='launch'){const s=game.launch;ctx.fillStyle='#060c1ac9';ctx.fillRect(260,20,480,50);drawText(s.ignited?'FLIGHT CONTROL · ACTIVE':'READY FOR IGNITION',500,42,12,s.ignited?'#8bf5bc':'#ffd874','center');drawText(s.ignited?'HOLD SAFE THROTTLE AND ATTITUDE':'PRESS SPACE OR IGNITION BUTTON',500,60,10,'#c8d8ed','center');}if(game.scene==='landing'){const s=game.landing;drawText('TARGET PAD',500,420,11,'#a7ffd0','center');ctx.strokeStyle='#7effb4';ctx.lineWidth=2;ctx.setLineDash([5,5]);ctx.strokeRect(430,440,140,45);ctx.setLineDash([]);}if(paused){ctx.fillStyle='#030713aa';ctx.fillRect(0,0,WIDTH,HEIGHT);drawText('PAUSED',WIDTH/2,HEIGHT/2,27,'#edf6ff','center');}}
function frame(now){if(!previousTime)previousTime=now;const dt=Math.min(.04,Math.max(0,(now-previousTime)/1000));previousTime=now;if(!paused)updateGame(dt);render();animationId=requestAnimationFrame(frame);}
game=freshGame();loadAtlas();setScene('menu');updateHud();$('overlay').classList.remove('hidden');animationId=requestAnimationFrame(frame);
</script>
</body>
</html>"""
SPACE_ATLAS = [
    {
        "id": "NAV-0001",
        "x": 1596,
        "y": 419,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0002",
        "x": 1857,
        "y": 280,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0003",
        "x": 1767,
        "y": 211,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0004",
        "x": 1803,
        "y": 132,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0005",
        "x": 509,
        "y": 232,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0006",
        "x": 3107,
        "y": 364,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0007",
        "x": 1628,
        "y": 277,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0008",
        "x": 544,
        "y": 17,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0009",
        "x": 265,
        "y": 188,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0010",
        "x": 2255,
        "y": 17,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0011",
        "x": 465,
        "y": 42,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0012",
        "x": 875,
        "y": 383,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0013",
        "x": 0,
        "y": 201,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0014",
        "x": 1905,
        "y": 14,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0015",
        "x": 755,
        "y": 261,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0016",
        "x": 2994,
        "y": 221,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0017",
        "x": 2203,
        "y": 198,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0018",
        "x": 1772,
        "y": 262,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0019",
        "x": 1505,
        "y": 363,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0020",
        "x": 1554,
        "y": 396,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0021",
        "x": 269,
        "y": 241,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0022",
        "x": 3110,
        "y": 121,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0023",
        "x": 823,
        "y": 64,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0024",
        "x": 2230,
        "y": 33,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0025",
        "x": 1504,
        "y": 423,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0026",
        "x": 805,
        "y": 163,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0027",
        "x": 2253,
        "y": 60,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0028",
        "x": 2866,
        "y": 421,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0029",
        "x": 2439,
        "y": 18,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0030",
        "x": 3,
        "y": 126,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0031",
        "x": 294,
        "y": 99,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0032",
        "x": 2001,
        "y": 371,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0033",
        "x": 915,
        "y": 389,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0034",
        "x": 3014,
        "y": 293,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0035",
        "x": 1053,
        "y": 215,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0036",
        "x": 3017,
        "y": 284,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0037",
        "x": 2040,
        "y": 367,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0038",
        "x": 2666,
        "y": 371,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0039",
        "x": 1978,
        "y": 176,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0040",
        "x": 283,
        "y": 117,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0041",
        "x": 214,
        "y": 173,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0042",
        "x": 2501,
        "y": 266,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0043",
        "x": 895,
        "y": 84,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0044",
        "x": 3053,
        "y": 373,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0045",
        "x": 1983,
        "y": 258,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0046",
        "x": 2804,
        "y": 266,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0047",
        "x": 2092,
        "y": 15,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0048",
        "x": 2037,
        "y": 23,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0049",
        "x": 1354,
        "y": 140,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0050",
        "x": 2592,
        "y": 418,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0051",
        "x": 216,
        "y": 186,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0052",
        "x": 2229,
        "y": 139,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0053",
        "x": 1726,
        "y": 171,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0054",
        "x": 808,
        "y": 328,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0055",
        "x": 2141,
        "y": 122,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0056",
        "x": 1926,
        "y": 421,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0057",
        "x": 2501,
        "y": 262,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0058",
        "x": 1520,
        "y": 213,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0059",
        "x": 886,
        "y": 132,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0060",
        "x": 3170,
        "y": 82,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0061",
        "x": 215,
        "y": 340,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0062",
        "x": 768,
        "y": 97,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0063",
        "x": 2670,
        "y": 191,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0064",
        "x": 2235,
        "y": 80,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0065",
        "x": 2360,
        "y": 129,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0066",
        "x": 1177,
        "y": 226,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0067",
        "x": 177,
        "y": 277,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0068",
        "x": 866,
        "y": 222,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0069",
        "x": 457,
        "y": 415,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0070",
        "x": 3176,
        "y": 240,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0071",
        "x": 430,
        "y": 190,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0072",
        "x": 3146,
        "y": 24,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0073",
        "x": 845,
        "y": 240,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0074",
        "x": 3071,
        "y": 368,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0075",
        "x": 2187,
        "y": 54,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0076",
        "x": 1564,
        "y": 326,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0077",
        "x": 1546,
        "y": 255,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0078",
        "x": 2784,
        "y": 307,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0079",
        "x": 884,
        "y": 100,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0080",
        "x": 4,
        "y": 56,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0081",
        "x": 2821,
        "y": 400,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0082",
        "x": 1814,
        "y": 47,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0083",
        "x": 1355,
        "y": 61,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0084",
        "x": 972,
        "y": 323,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0085",
        "x": 819,
        "y": 396,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0086",
        "x": 3159,
        "y": 173,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0087",
        "x": 980,
        "y": 258,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0088",
        "x": 11,
        "y": 216,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0089",
        "x": 763,
        "y": 328,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0090",
        "x": 3001,
        "y": 265,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0091",
        "x": 2795,
        "y": 188,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0092",
        "x": 3025,
        "y": 151,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0093",
        "x": 2161,
        "y": 296,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0094",
        "x": 61,
        "y": 56,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0095",
        "x": 2113,
        "y": 275,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0096",
        "x": 1818,
        "y": 71,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0097",
        "x": 2711,
        "y": 344,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0098",
        "x": 1568,
        "y": 159,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0099",
        "x": 2445,
        "y": 413,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0100",
        "x": 1176,
        "y": 226,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0101",
        "x": 610,
        "y": 299,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0102",
        "x": 637,
        "y": 278,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0103",
        "x": 1130,
        "y": 136,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0104",
        "x": 734,
        "y": 356,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0105",
        "x": 2368,
        "y": 404,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0106",
        "x": 2006,
        "y": 62,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0107",
        "x": 1433,
        "y": 251,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0108",
        "x": 1707,
        "y": 195,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0109",
        "x": 2127,
        "y": 309,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0110",
        "x": 1492,
        "y": 425,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0111",
        "x": 3153,
        "y": 282,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0112",
        "x": 1587,
        "y": 377,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0113",
        "x": 1065,
        "y": 363,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0114",
        "x": 2038,
        "y": 324,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0115",
        "x": 2887,
        "y": 384,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0116",
        "x": 1139,
        "y": 26,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0117",
        "x": 2798,
        "y": 116,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0118",
        "x": 1330,
        "y": 56,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0119",
        "x": 353,
        "y": 277,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0120",
        "x": 2521,
        "y": 275,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0121",
        "x": 2753,
        "y": 385,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0122",
        "x": 3152,
        "y": 187,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0123",
        "x": 2655,
        "y": 193,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0124",
        "x": 2278,
        "y": 283,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0125",
        "x": 1009,
        "y": 226,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0126",
        "x": 2254,
        "y": 358,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0127",
        "x": 1415,
        "y": 104,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0128",
        "x": 1725,
        "y": 362,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0129",
        "x": 2473,
        "y": 223,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0130",
        "x": 1444,
        "y": 363,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0131",
        "x": 1072,
        "y": 191,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0132",
        "x": 140,
        "y": 122,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0133",
        "x": 1962,
        "y": 330,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0134",
        "x": 1979,
        "y": 217,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0135",
        "x": 2320,
        "y": 344,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0136",
        "x": 274,
        "y": 354,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0137",
        "x": 274,
        "y": 350,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0138",
        "x": 2433,
        "y": 247,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0139",
        "x": 2730,
        "y": 200,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0140",
        "x": 1500,
        "y": 299,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0141",
        "x": 2250,
        "y": 211,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0142",
        "x": 151,
        "y": 361,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0143",
        "x": 2806,
        "y": 8,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0144",
        "x": 2583,
        "y": 181,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0145",
        "x": 1338,
        "y": 225,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0146",
        "x": 2871,
        "y": 209,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0147",
        "x": 166,
        "y": 87,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0148",
        "x": 2913,
        "y": 197,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0149",
        "x": 97,
        "y": 76,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0150",
        "x": 1792,
        "y": 379,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0151",
        "x": 1455,
        "y": 116,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0152",
        "x": 1701,
        "y": 230,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0153",
        "x": 2314,
        "y": 116,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0154",
        "x": 2229,
        "y": 370,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0155",
        "x": 2406,
        "y": 399,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0156",
        "x": 1401,
        "y": 190,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0157",
        "x": 1621,
        "y": 317,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0158",
        "x": 2502,
        "y": 237,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0159",
        "x": 3108,
        "y": 114,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0160",
        "x": 2006,
        "y": 36,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0161",
        "x": 765,
        "y": 202,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0162",
        "x": 2815,
        "y": 369,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0163",
        "x": 2585,
        "y": 242,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0164",
        "x": 477,
        "y": 172,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0165",
        "x": 2766,
        "y": 61,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0166",
        "x": 1753,
        "y": 234,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0167",
        "x": 968,
        "y": 287,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0168",
        "x": 951,
        "y": 234,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0169",
        "x": 2577,
        "y": 103,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0170",
        "x": 2822,
        "y": 38,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0171",
        "x": 3119,
        "y": 194,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0172",
        "x": 1143,
        "y": 126,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0173",
        "x": 345,
        "y": 12,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0174",
        "x": 2453,
        "y": 119,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0175",
        "x": 2498,
        "y": 231,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0176",
        "x": 190,
        "y": 82,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0177",
        "x": 206,
        "y": 170,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0178",
        "x": 2504,
        "y": 399,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0179",
        "x": 2456,
        "y": 316,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0180",
        "x": 596,
        "y": 422,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0181",
        "x": 641,
        "y": 310,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0182",
        "x": 1363,
        "y": 216,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0183",
        "x": 1597,
        "y": 92,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0184",
        "x": 2904,
        "y": 99,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0185",
        "x": 2287,
        "y": 294,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0186",
        "x": 2363,
        "y": 244,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0187",
        "x": 2236,
        "y": 64,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0188",
        "x": 3119,
        "y": 117,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0189",
        "x": 1761,
        "y": 26,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0190",
        "x": 51,
        "y": 314,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0191",
        "x": 3147,
        "y": 52,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0192",
        "x": 3099,
        "y": 116,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0193",
        "x": 3128,
        "y": 396,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0194",
        "x": 1676,
        "y": 252,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0195",
        "x": 234,
        "y": 53,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0196",
        "x": 1064,
        "y": 169,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0197",
        "x": 1214,
        "y": 137,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0198",
        "x": 1543,
        "y": 176,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0199",
        "x": 1159,
        "y": 341,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0200",
        "x": 784,
        "y": 73,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0201",
        "x": 1569,
        "y": 291,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0202",
        "x": 896,
        "y": 236,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0203",
        "x": 1499,
        "y": 134,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0204",
        "x": 2962,
        "y": 282,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0205",
        "x": 354,
        "y": 50,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0206",
        "x": 357,
        "y": 357,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0207",
        "x": 1657,
        "y": 338,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0208",
        "x": 846,
        "y": 77,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0209",
        "x": 2764,
        "y": 150,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0210",
        "x": 1926,
        "y": 314,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0211",
        "x": 2639,
        "y": 113,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0212",
        "x": 2418,
        "y": 358,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0213",
        "x": 561,
        "y": 355,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0214",
        "x": 1124,
        "y": 36,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0215",
        "x": 1766,
        "y": 252,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0216",
        "x": 856,
        "y": 230,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0217",
        "x": 2848,
        "y": 128,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0218",
        "x": 1848,
        "y": 128,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0219",
        "x": 1610,
        "y": 30,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0220",
        "x": 203,
        "y": 49,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0221",
        "x": 3060,
        "y": 404,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0222",
        "x": 27,
        "y": 86,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0223",
        "x": 2760,
        "y": 303,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0224",
        "x": 1014,
        "y": 171,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0225",
        "x": 382,
        "y": 60,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0226",
        "x": 3077,
        "y": 98,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0227",
        "x": 2577,
        "y": 117,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0228",
        "x": 1373,
        "y": 187,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0229",
        "x": 2557,
        "y": 229,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0230",
        "x": 2849,
        "y": 203,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0231",
        "x": 949,
        "y": 239,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0232",
        "x": 1234,
        "y": 356,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0233",
        "x": 1683,
        "y": 416,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0234",
        "x": 1719,
        "y": 94,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0235",
        "x": 913,
        "y": 157,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0236",
        "x": 2178,
        "y": 261,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0237",
        "x": 1454,
        "y": 142,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0238",
        "x": 2524,
        "y": 160,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0239",
        "x": 94,
        "y": 112,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0240",
        "x": 528,
        "y": 172,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0241",
        "x": 2606,
        "y": 427,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0242",
        "x": 99,
        "y": 278,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0243",
        "x": 831,
        "y": 188,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0244",
        "x": 1756,
        "y": 242,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0245",
        "x": 2792,
        "y": 414,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0246",
        "x": 2171,
        "y": 221,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0247",
        "x": 1108,
        "y": 401,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0248",
        "x": 2325,
        "y": 413,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0249",
        "x": 92,
        "y": 13,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0250",
        "x": 2655,
        "y": 404,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0251",
        "x": 2927,
        "y": 39,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0252",
        "x": 2899,
        "y": 310,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0253",
        "x": 2251,
        "y": 406,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0254",
        "x": 3129,
        "y": 305,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0255",
        "x": 3069,
        "y": 29,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0256",
        "x": 838,
        "y": 12,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0257",
        "x": 2677,
        "y": 135,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0258",
        "x": 960,
        "y": 33,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0259",
        "x": 1996,
        "y": 369,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0260",
        "x": 692,
        "y": 196,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0261",
        "x": 1496,
        "y": 283,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0262",
        "x": 2934,
        "y": 146,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0263",
        "x": 323,
        "y": 394,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0264",
        "x": 2150,
        "y": 343,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0265",
        "x": 489,
        "y": 383,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0266",
        "x": 1056,
        "y": 100,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0267",
        "x": 2012,
        "y": 260,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0268",
        "x": 2080,
        "y": 414,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0269",
        "x": 2105,
        "y": 272,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0270",
        "x": 1137,
        "y": 84,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0271",
        "x": 388,
        "y": 339,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0272",
        "x": 2392,
        "y": 390,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0273",
        "x": 2587,
        "y": 164,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0274",
        "x": 115,
        "y": 383,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0275",
        "x": 3130,
        "y": 269,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0276",
        "x": 924,
        "y": 218,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0277",
        "x": 2067,
        "y": 391,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0278",
        "x": 2604,
        "y": 341,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0279",
        "x": 1586,
        "y": 239,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0280",
        "x": 2337,
        "y": 406,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0281",
        "x": 300,
        "y": 54,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0282",
        "x": 1755,
        "y": 318,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0283",
        "x": 847,
        "y": 95,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0284",
        "x": 68,
        "y": 417,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0285",
        "x": 763,
        "y": 328,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0286",
        "x": 128,
        "y": 423,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0287",
        "x": 1731,
        "y": 376,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0288",
        "x": 1671,
        "y": 317,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0289",
        "x": 1765,
        "y": 407,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0290",
        "x": 1964,
        "y": 367,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0291",
        "x": 978,
        "y": 163,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0292",
        "x": 2428,
        "y": 45,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0293",
        "x": 2705,
        "y": 427,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0294",
        "x": 1092,
        "y": 106,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0295",
        "x": 923,
        "y": 71,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0296",
        "x": 2073,
        "y": 334,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0297",
        "x": 2787,
        "y": 118,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0298",
        "x": 292,
        "y": 405,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0299",
        "x": 1720,
        "y": 279,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0300",
        "x": 986,
        "y": 224,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0301",
        "x": 68,
        "y": 282,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0302",
        "x": 167,
        "y": 151,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0303",
        "x": 3048,
        "y": 358,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0304",
        "x": 61,
        "y": 375,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0305",
        "x": 2357,
        "y": 326,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0306",
        "x": 876,
        "y": 338,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0307",
        "x": 1990,
        "y": 257,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0308",
        "x": 160,
        "y": 213,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0309",
        "x": 923,
        "y": 273,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0310",
        "x": 911,
        "y": 223,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0311",
        "x": 2080,
        "y": 18,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0312",
        "x": 797,
        "y": 43,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0313",
        "x": 1520,
        "y": 187,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0314",
        "x": 1790,
        "y": 427,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0315",
        "x": 2170,
        "y": 280,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0316",
        "x": 270,
        "y": 412,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0317",
        "x": 1994,
        "y": 366,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0318",
        "x": 2455,
        "y": 307,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0319",
        "x": 1469,
        "y": 138,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0320",
        "x": 1872,
        "y": 411,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0321",
        "x": 750,
        "y": 278,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0322",
        "x": 3122,
        "y": 167,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0323",
        "x": 1530,
        "y": 173,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0324",
        "x": 2657,
        "y": 325,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0325",
        "x": 1429,
        "y": 266,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0326",
        "x": 1359,
        "y": 362,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0327",
        "x": 2919,
        "y": 356,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0328",
        "x": 2742,
        "y": 204,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0329",
        "x": 2047,
        "y": 211,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0330",
        "x": 330,
        "y": 255,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0331",
        "x": 2115,
        "y": 267,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0332",
        "x": 405,
        "y": 131,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0333",
        "x": 831,
        "y": 235,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0334",
        "x": 2458,
        "y": 350,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0335",
        "x": 2158,
        "y": 348,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0336",
        "x": 1778,
        "y": 49,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0337",
        "x": 278,
        "y": 314,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0338",
        "x": 2264,
        "y": 226,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0339",
        "x": 2203,
        "y": 111,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0340",
        "x": 1419,
        "y": 161,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0341",
        "x": 3193,
        "y": 113,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0342",
        "x": 2610,
        "y": 55,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0343",
        "x": 1137,
        "y": 113,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0344",
        "x": 2452,
        "y": 63,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0345",
        "x": 1662,
        "y": 96,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0346",
        "x": 2106,
        "y": 375,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0347",
        "x": 1137,
        "y": 39,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0348",
        "x": 321,
        "y": 10,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0349",
        "x": 1794,
        "y": 139,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0350",
        "x": 3106,
        "y": 423,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0351",
        "x": 2560,
        "y": 107,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0352",
        "x": 1496,
        "y": 352,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0353",
        "x": 894,
        "y": 327,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0354",
        "x": 1890,
        "y": 327,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0355",
        "x": 2279,
        "y": 372,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0356",
        "x": 309,
        "y": 195,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0357",
        "x": 369,
        "y": 235,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0358",
        "x": 1572,
        "y": 418,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0359",
        "x": 1067,
        "y": 299,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0360",
        "x": 1640,
        "y": 404,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0361",
        "x": 3092,
        "y": 156,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0362",
        "x": 1618,
        "y": 22,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0363",
        "x": 216,
        "y": 131,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0364",
        "x": 1089,
        "y": 217,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0365",
        "x": 420,
        "y": 52,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0366",
        "x": 2822,
        "y": 252,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0367",
        "x": 161,
        "y": 122,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0368",
        "x": 2214,
        "y": 177,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0369",
        "x": 2010,
        "y": 50,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0370",
        "x": 3127,
        "y": 197,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0371",
        "x": 1437,
        "y": 109,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0372",
        "x": 215,
        "y": 147,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0373",
        "x": 2618,
        "y": 380,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0374",
        "x": 2202,
        "y": 130,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0375",
        "x": 1207,
        "y": 96,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0376",
        "x": 1328,
        "y": 421,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0377",
        "x": 2336,
        "y": 35,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0378",
        "x": 754,
        "y": 196,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0379",
        "x": 189,
        "y": 17,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0380",
        "x": 2823,
        "y": 104,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0381",
        "x": 135,
        "y": 194,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0382",
        "x": 1239,
        "y": 28,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0383",
        "x": 1189,
        "y": 104,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0384",
        "x": 3160,
        "y": 230,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0385",
        "x": 2389,
        "y": 401,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0386",
        "x": 34,
        "y": 161,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0387",
        "x": 1608,
        "y": 332,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0388",
        "x": 3170,
        "y": 309,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0389",
        "x": 1736,
        "y": 77,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0390",
        "x": 3165,
        "y": 263,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0391",
        "x": 1581,
        "y": 199,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0392",
        "x": 2449,
        "y": 44,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0393",
        "x": 2439,
        "y": 223,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0394",
        "x": 2423,
        "y": 242,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0395",
        "x": 466,
        "y": 252,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0396",
        "x": 1604,
        "y": 69,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0397",
        "x": 2478,
        "y": 195,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0398",
        "x": 1832,
        "y": 313,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0399",
        "x": 202,
        "y": 311,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0400",
        "x": 1625,
        "y": 323,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0401",
        "x": 2282,
        "y": 128,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0402",
        "x": 607,
        "y": 114,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0403",
        "x": 383,
        "y": 15,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0404",
        "x": 1724,
        "y": 320,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0405",
        "x": 380,
        "y": 52,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0406",
        "x": 2857,
        "y": 420,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0407",
        "x": 1660,
        "y": 408,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0408",
        "x": 145,
        "y": 379,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0409",
        "x": 3156,
        "y": 252,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0410",
        "x": 2433,
        "y": 281,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0411",
        "x": 3115,
        "y": 356,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0412",
        "x": 2937,
        "y": 290,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0413",
        "x": 1711,
        "y": 121,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0414",
        "x": 852,
        "y": 380,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0415",
        "x": 894,
        "y": 326,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0416",
        "x": 2794,
        "y": 72,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0417",
        "x": 547,
        "y": 182,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0418",
        "x": 2260,
        "y": 185,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0419",
        "x": 1994,
        "y": 250,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0420",
        "x": 2955,
        "y": 353,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0421",
        "x": 836,
        "y": 52,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0422",
        "x": 1954,
        "y": 103,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0423",
        "x": 1967,
        "y": 313,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0424",
        "x": 2004,
        "y": 49,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0425",
        "x": 2233,
        "y": 209,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0426",
        "x": 2436,
        "y": 166,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0427",
        "x": 2698,
        "y": 203,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0428",
        "x": 1458,
        "y": 421,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0429",
        "x": 3097,
        "y": 204,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0430",
        "x": 2659,
        "y": 222,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0431",
        "x": 2603,
        "y": 381,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0432",
        "x": 1925,
        "y": 280,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0433",
        "x": 614,
        "y": 116,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0434",
        "x": 1155,
        "y": 138,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0435",
        "x": 2848,
        "y": 210,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0436",
        "x": 2719,
        "y": 384,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0437",
        "x": 662,
        "y": 175,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0438",
        "x": 1539,
        "y": 50,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0439",
        "x": 112,
        "y": 88,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0440",
        "x": 677,
        "y": 171,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0441",
        "x": 322,
        "y": 107,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0442",
        "x": 882,
        "y": 359,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0443",
        "x": 1061,
        "y": 86,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0444",
        "x": 622,
        "y": 70,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0445",
        "x": 2240,
        "y": 98,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0446",
        "x": 1287,
        "y": 386,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0447",
        "x": 164,
        "y": 194,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0448",
        "x": 2480,
        "y": 417,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0449",
        "x": 1379,
        "y": 150,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0450",
        "x": 169,
        "y": 395,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0451",
        "x": 1938,
        "y": 205,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0452",
        "x": 723,
        "y": 70,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0453",
        "x": 771,
        "y": 423,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0454",
        "x": 1691,
        "y": 27,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0455",
        "x": 2542,
        "y": 46,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0456",
        "x": 1440,
        "y": 179,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0457",
        "x": 8,
        "y": 260,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0458",
        "x": 3199,
        "y": 185,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0459",
        "x": 385,
        "y": 53,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0460",
        "x": 2692,
        "y": 233,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0461",
        "x": 2529,
        "y": 329,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0462",
        "x": 1972,
        "y": 360,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0463",
        "x": 1710,
        "y": 309,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0464",
        "x": 2701,
        "y": 33,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0465",
        "x": 1540,
        "y": 55,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0466",
        "x": 2441,
        "y": 194,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0467",
        "x": 655,
        "y": 306,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0468",
        "x": 348,
        "y": 135,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0469",
        "x": 2411,
        "y": 328,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0470",
        "x": 462,
        "y": 253,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0471",
        "x": 539,
        "y": 11,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0472",
        "x": 13,
        "y": 121,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0473",
        "x": 2330,
        "y": 408,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0474",
        "x": 810,
        "y": 329,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0475",
        "x": 1003,
        "y": 298,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0476",
        "x": 1841,
        "y": 411,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0477",
        "x": 2766,
        "y": 27,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0478",
        "x": 2933,
        "y": 89,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0479",
        "x": 2331,
        "y": 201,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0480",
        "x": 2466,
        "y": 121,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0481",
        "x": 1982,
        "y": 9,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0482",
        "x": 2701,
        "y": 413,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0483",
        "x": 2262,
        "y": 223,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0484",
        "x": 1608,
        "y": 31,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0485",
        "x": 2905,
        "y": 117,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0486",
        "x": 15,
        "y": 302,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0487",
        "x": 2136,
        "y": 260,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0488",
        "x": 852,
        "y": 425,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0489",
        "x": 2171,
        "y": 34,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0490",
        "x": 204,
        "y": 81,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0491",
        "x": 1129,
        "y": 231,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0492",
        "x": 1241,
        "y": 381,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0493",
        "x": 3064,
        "y": 300,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0494",
        "x": 2799,
        "y": 406,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0495",
        "x": 2814,
        "y": 304,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0496",
        "x": 975,
        "y": 357,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0497",
        "x": 432,
        "y": 343,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0498",
        "x": 2930,
        "y": 278,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0499",
        "x": 1241,
        "y": 291,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0500",
        "x": 1419,
        "y": 417,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0501",
        "x": 2314,
        "y": 77,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0502",
        "x": 629,
        "y": 156,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0503",
        "x": 1820,
        "y": 361,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0504",
        "x": 502,
        "y": 54,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0505",
        "x": 553,
        "y": 269,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0506",
        "x": 2345,
        "y": 11,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0507",
        "x": 359,
        "y": 77,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0508",
        "x": 1749,
        "y": 314,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0509",
        "x": 2207,
        "y": 380,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0510",
        "x": 1641,
        "y": 414,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0511",
        "x": 8,
        "y": 266,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0512",
        "x": 1116,
        "y": 401,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0513",
        "x": 2028,
        "y": 265,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0514",
        "x": 1539,
        "y": 402,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0515",
        "x": 587,
        "y": 50,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0516",
        "x": 908,
        "y": 174,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0517",
        "x": 3071,
        "y": 337,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0518",
        "x": 1707,
        "y": 309,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0519",
        "x": 2455,
        "y": 53,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0520",
        "x": 2148,
        "y": 161,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0521",
        "x": 1168,
        "y": 346,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0522",
        "x": 402,
        "y": 118,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0523",
        "x": 458,
        "y": 413,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0524",
        "x": 1688,
        "y": 378,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0525",
        "x": 818,
        "y": 138,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0526",
        "x": 2395,
        "y": 341,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0527",
        "x": 1114,
        "y": 389,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0528",
        "x": 757,
        "y": 8,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0529",
        "x": 2481,
        "y": 306,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0530",
        "x": 2661,
        "y": 364,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0531",
        "x": 2885,
        "y": 92,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0532",
        "x": 605,
        "y": 384,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0533",
        "x": 227,
        "y": 72,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0534",
        "x": 26,
        "y": 281,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0535",
        "x": 1442,
        "y": 399,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0536",
        "x": 2693,
        "y": 184,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0537",
        "x": 866,
        "y": 402,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0538",
        "x": 3102,
        "y": 417,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0539",
        "x": 2956,
        "y": 13,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0540",
        "x": 243,
        "y": 244,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0541",
        "x": 2914,
        "y": 39,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0542",
        "x": 73,
        "y": 294,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0543",
        "x": 1567,
        "y": 58,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0544",
        "x": 135,
        "y": 389,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0545",
        "x": 2289,
        "y": 96,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0546",
        "x": 2408,
        "y": 134,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0547",
        "x": 750,
        "y": 357,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0548",
        "x": 1037,
        "y": 371,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0549",
        "x": 2385,
        "y": 91,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0550",
        "x": 1159,
        "y": 385,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0551",
        "x": 226,
        "y": 181,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0552",
        "x": 1411,
        "y": 59,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0553",
        "x": 2240,
        "y": 39,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0554",
        "x": 1405,
        "y": 387,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0555",
        "x": 2346,
        "y": 172,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0556",
        "x": 581,
        "y": 153,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0557",
        "x": 3138,
        "y": 104,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0558",
        "x": 741,
        "y": 230,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0559",
        "x": 1135,
        "y": 130,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0560",
        "x": 2570,
        "y": 296,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0561",
        "x": 2073,
        "y": 105,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0562",
        "x": 844,
        "y": 389,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0563",
        "x": 1186,
        "y": 363,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0564",
        "x": 1317,
        "y": 165,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0565",
        "x": 1847,
        "y": 86,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0566",
        "x": 1454,
        "y": 178,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0567",
        "x": 102,
        "y": 337,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0568",
        "x": 435,
        "y": 426,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0569",
        "x": 562,
        "y": 413,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0570",
        "x": 458,
        "y": 225,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0571",
        "x": 839,
        "y": 264,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0572",
        "x": 505,
        "y": 262,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0573",
        "x": 477,
        "y": 248,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0574",
        "x": 726,
        "y": 338,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0575",
        "x": 2283,
        "y": 294,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0576",
        "x": 419,
        "y": 237,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0577",
        "x": 1504,
        "y": 326,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0578",
        "x": 1743,
        "y": 427,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0579",
        "x": 213,
        "y": 44,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0580",
        "x": 2529,
        "y": 96,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0581",
        "x": 769,
        "y": 254,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0582",
        "x": 2378,
        "y": 75,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0583",
        "x": 2486,
        "y": 352,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0584",
        "x": 1762,
        "y": 246,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0585",
        "x": 2531,
        "y": 271,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0586",
        "x": 688,
        "y": 45,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0587",
        "x": 2539,
        "y": 68,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0588",
        "x": 2016,
        "y": 177,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0589",
        "x": 332,
        "y": 138,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0590",
        "x": 1683,
        "y": 98,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0591",
        "x": 619,
        "y": 291,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0592",
        "x": 703,
        "y": 326,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0593",
        "x": 1245,
        "y": 296,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0594",
        "x": 2539,
        "y": 349,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0595",
        "x": 2437,
        "y": 91,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0596",
        "x": 1584,
        "y": 263,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0597",
        "x": 2292,
        "y": 374,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0598",
        "x": 8,
        "y": 8,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0599",
        "x": 960,
        "y": 200,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0600",
        "x": 2260,
        "y": 369,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0601",
        "x": 2867,
        "y": 349,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0602",
        "x": 2745,
        "y": 10,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0603",
        "x": 630,
        "y": 213,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0604",
        "x": 2654,
        "y": 410,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0605",
        "x": 2700,
        "y": 161,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0606",
        "x": 1756,
        "y": 413,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0607",
        "x": 1190,
        "y": 222,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0608",
        "x": 495,
        "y": 395,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0609",
        "x": 693,
        "y": 227,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0610",
        "x": 1408,
        "y": 14,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0611",
        "x": 1394,
        "y": 33,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0612",
        "x": 1638,
        "y": 265,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0613",
        "x": 144,
        "y": 136,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0614",
        "x": 302,
        "y": 184,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0615",
        "x": 234,
        "y": 357,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0616",
        "x": 2353,
        "y": 24,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0617",
        "x": 3067,
        "y": 33,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0618",
        "x": 2673,
        "y": 199,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0619",
        "x": 3152,
        "y": 410,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0620",
        "x": 1169,
        "y": 196,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0621",
        "x": 2120,
        "y": 309,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0622",
        "x": 707,
        "y": 279,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0623",
        "x": 936,
        "y": 137,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0624",
        "x": 2090,
        "y": 34,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0625",
        "x": 360,
        "y": 112,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0626",
        "x": 2011,
        "y": 291,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0627",
        "x": 564,
        "y": 18,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0628",
        "x": 1106,
        "y": 215,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0629",
        "x": 680,
        "y": 378,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0630",
        "x": 1217,
        "y": 129,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0631",
        "x": 3022,
        "y": 275,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0632",
        "x": 1266,
        "y": 221,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0633",
        "x": 2347,
        "y": 330,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0634",
        "x": 2768,
        "y": 153,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0635",
        "x": 2406,
        "y": 138,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0636",
        "x": 3193,
        "y": 312,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0637",
        "x": 1941,
        "y": 246,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0638",
        "x": 1008,
        "y": 389,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0639",
        "x": 1041,
        "y": 182,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0640",
        "x": 2615,
        "y": 65,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0641",
        "x": 1107,
        "y": 292,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0642",
        "x": 2558,
        "y": 385,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0643",
        "x": 2466,
        "y": 365,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0644",
        "x": 1104,
        "y": 250,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0645",
        "x": 286,
        "y": 309,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0646",
        "x": 2690,
        "y": 120,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0647",
        "x": 2942,
        "y": 251,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0648",
        "x": 1547,
        "y": 370,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0649",
        "x": 248,
        "y": 211,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0650",
        "x": 134,
        "y": 375,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0651",
        "x": 2488,
        "y": 86,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0652",
        "x": 2284,
        "y": 334,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0653",
        "x": 2061,
        "y": 148,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0654",
        "x": 263,
        "y": 345,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0655",
        "x": 1021,
        "y": 360,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0656",
        "x": 1071,
        "y": 117,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0657",
        "x": 3016,
        "y": 428,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0658",
        "x": 2791,
        "y": 123,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0659",
        "x": 1386,
        "y": 173,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0660",
        "x": 1698,
        "y": 258,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0661",
        "x": 2248,
        "y": 130,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0662",
        "x": 2849,
        "y": 245,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0663",
        "x": 869,
        "y": 45,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0664",
        "x": 2811,
        "y": 85,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0665",
        "x": 593,
        "y": 65,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0666",
        "x": 466,
        "y": 46,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0667",
        "x": 1459,
        "y": 8,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0668",
        "x": 1495,
        "y": 331,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0669",
        "x": 787,
        "y": 262,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0670",
        "x": 1721,
        "y": 313,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0671",
        "x": 2107,
        "y": 105,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0672",
        "x": 1085,
        "y": 395,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0673",
        "x": 631,
        "y": 347,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0674",
        "x": 1301,
        "y": 326,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0675",
        "x": 671,
        "y": 150,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0676",
        "x": 2462,
        "y": 125,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0677",
        "x": 1888,
        "y": 70,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0678",
        "x": 2032,
        "y": 380,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0679",
        "x": 2009,
        "y": 26,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0680",
        "x": 1938,
        "y": 236,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0681",
        "x": 426,
        "y": 98,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0682",
        "x": 2587,
        "y": 422,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0683",
        "x": 1586,
        "y": 12,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0684",
        "x": 1298,
        "y": 110,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0685",
        "x": 2932,
        "y": 383,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0686",
        "x": 2358,
        "y": 266,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0687",
        "x": 3046,
        "y": 297,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0688",
        "x": 2105,
        "y": 26,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0689",
        "x": 1540,
        "y": 267,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0690",
        "x": 1065,
        "y": 48,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0691",
        "x": 393,
        "y": 342,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0692",
        "x": 1126,
        "y": 187,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0693",
        "x": 933,
        "y": 235,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0694",
        "x": 1288,
        "y": 364,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0695",
        "x": 127,
        "y": 359,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0696",
        "x": 1664,
        "y": 179,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0697",
        "x": 3038,
        "y": 392,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0698",
        "x": 2430,
        "y": 282,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0699",
        "x": 137,
        "y": 304,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0700",
        "x": 414,
        "y": 296,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0701",
        "x": 63,
        "y": 394,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0702",
        "x": 1640,
        "y": 115,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0703",
        "x": 261,
        "y": 209,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0704",
        "x": 1031,
        "y": 336,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0705",
        "x": 2287,
        "y": 170,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0706",
        "x": 2393,
        "y": 411,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0707",
        "x": 76,
        "y": 207,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0708",
        "x": 532,
        "y": 336,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0709",
        "x": 2403,
        "y": 182,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0710",
        "x": 2043,
        "y": 217,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0711",
        "x": 1936,
        "y": 294,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0712",
        "x": 3018,
        "y": 327,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0713",
        "x": 672,
        "y": 347,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0714",
        "x": 113,
        "y": 361,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0715",
        "x": 778,
        "y": 248,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0716",
        "x": 1889,
        "y": 134,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0717",
        "x": 1987,
        "y": 148,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0718",
        "x": 2884,
        "y": 420,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0719",
        "x": 1963,
        "y": 414,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0720",
        "x": 903,
        "y": 53,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0721",
        "x": 109,
        "y": 363,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0722",
        "x": 1800,
        "y": 372,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0723",
        "x": 695,
        "y": 316,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0724",
        "x": 2281,
        "y": 347,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0725",
        "x": 213,
        "y": 363,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0726",
        "x": 3143,
        "y": 296,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0727",
        "x": 2660,
        "y": 65,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0728",
        "x": 121,
        "y": 404,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0729",
        "x": 1005,
        "y": 375,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0730",
        "x": 2956,
        "y": 13,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0731",
        "x": 2156,
        "y": 34,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0732",
        "x": 1388,
        "y": 302,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0733",
        "x": 1391,
        "y": 386,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0734",
        "x": 2710,
        "y": 101,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0735",
        "x": 2862,
        "y": 372,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0736",
        "x": 162,
        "y": 17,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0737",
        "x": 383,
        "y": 47,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0738",
        "x": 417,
        "y": 360,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0739",
        "x": 3005,
        "y": 404,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0740",
        "x": 1751,
        "y": 212,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0741",
        "x": 1424,
        "y": 385,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0742",
        "x": 1614,
        "y": 401,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0743",
        "x": 25,
        "y": 278,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0744",
        "x": 470,
        "y": 162,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0745",
        "x": 3146,
        "y": 87,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0746",
        "x": 1059,
        "y": 249,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0747",
        "x": 371,
        "y": 52,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0748",
        "x": 66,
        "y": 167,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0749",
        "x": 3124,
        "y": 321,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0750",
        "x": 1539,
        "y": 257,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0751",
        "x": 138,
        "y": 39,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0752",
        "x": 2624,
        "y": 189,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0753",
        "x": 1439,
        "y": 118,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0754",
        "x": 1426,
        "y": 323,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0755",
        "x": 562,
        "y": 405,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0756",
        "x": 883,
        "y": 57,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0757",
        "x": 1588,
        "y": 105,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0758",
        "x": 1847,
        "y": 282,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0759",
        "x": 560,
        "y": 272,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0760",
        "x": 2895,
        "y": 378,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0761",
        "x": 547,
        "y": 373,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0762",
        "x": 555,
        "y": 183,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0763",
        "x": 2826,
        "y": 17,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0764",
        "x": 633,
        "y": 205,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0765",
        "x": 3055,
        "y": 201,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0766",
        "x": 2255,
        "y": 170,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0767",
        "x": 2482,
        "y": 364,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0768",
        "x": 270,
        "y": 121,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0769",
        "x": 2344,
        "y": 221,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0770",
        "x": 1214,
        "y": 228,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0771",
        "x": 2147,
        "y": 65,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0772",
        "x": 1194,
        "y": 160,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0773",
        "x": 953,
        "y": 117,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0774",
        "x": 1316,
        "y": 31,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0775",
        "x": 145,
        "y": 21,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0776",
        "x": 857,
        "y": 240,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0777",
        "x": 1334,
        "y": 96,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0778",
        "x": 391,
        "y": 405,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0779",
        "x": 353,
        "y": 31,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0780",
        "x": 2249,
        "y": 19,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0781",
        "x": 2933,
        "y": 152,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0782",
        "x": 1522,
        "y": 39,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0783",
        "x": 611,
        "y": 378,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0784",
        "x": 529,
        "y": 9,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0785",
        "x": 2794,
        "y": 12,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0786",
        "x": 654,
        "y": 233,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0787",
        "x": 405,
        "y": 89,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0788",
        "x": 2490,
        "y": 318,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0789",
        "x": 2521,
        "y": 303,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0790",
        "x": 599,
        "y": 138,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0791",
        "x": 2228,
        "y": 42,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0792",
        "x": 536,
        "y": 209,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0793",
        "x": 1464,
        "y": 376,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0794",
        "x": 2692,
        "y": 206,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0795",
        "x": 769,
        "y": 416,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0796",
        "x": 118,
        "y": 237,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0797",
        "x": 628,
        "y": 49,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0798",
        "x": 1978,
        "y": 277,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0799",
        "x": 1530,
        "y": 90,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0800",
        "x": 2848,
        "y": 108,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0801",
        "x": 2686,
        "y": 159,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0802",
        "x": 479,
        "y": 28,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0803",
        "x": 2192,
        "y": 395,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0804",
        "x": 3062,
        "y": 94,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0805",
        "x": 2949,
        "y": 411,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0806",
        "x": 2477,
        "y": 318,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0807",
        "x": 1661,
        "y": 201,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0808",
        "x": 2881,
        "y": 166,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0809",
        "x": 3113,
        "y": 292,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0810",
        "x": 2162,
        "y": 18,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0811",
        "x": 1807,
        "y": 74,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0812",
        "x": 1152,
        "y": 261,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0813",
        "x": 739,
        "y": 60,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0814",
        "x": 374,
        "y": 237,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0815",
        "x": 199,
        "y": 160,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0816",
        "x": 2638,
        "y": 286,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0817",
        "x": 1563,
        "y": 36,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0818",
        "x": 2084,
        "y": 303,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0819",
        "x": 355,
        "y": 134,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0820",
        "x": 2992,
        "y": 154,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0821",
        "x": 1829,
        "y": 238,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0822",
        "x": 1493,
        "y": 75,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0823",
        "x": 2805,
        "y": 75,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0824",
        "x": 664,
        "y": 47,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0825",
        "x": 1393,
        "y": 47,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0826",
        "x": 2793,
        "y": 195,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0827",
        "x": 1344,
        "y": 399,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0828",
        "x": 1968,
        "y": 42,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0829",
        "x": 1137,
        "y": 324,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0830",
        "x": 577,
        "y": 163,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0831",
        "x": 1337,
        "y": 53,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0832",
        "x": 1558,
        "y": 83,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0833",
        "x": 676,
        "y": 365,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0834",
        "x": 1143,
        "y": 389,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0835",
        "x": 1277,
        "y": 390,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0836",
        "x": 2991,
        "y": 266,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0837",
        "x": 830,
        "y": 116,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0838",
        "x": 2319,
        "y": 371,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0839",
        "x": 183,
        "y": 355,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0840",
        "x": 766,
        "y": 28,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0841",
        "x": 1962,
        "y": 133,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0842",
        "x": 1455,
        "y": 214,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0843",
        "x": 3063,
        "y": 43,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0844",
        "x": 1189,
        "y": 388,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0845",
        "x": 3042,
        "y": 340,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0846",
        "x": 1890,
        "y": 171,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0847",
        "x": 1177,
        "y": 374,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0848",
        "x": 1430,
        "y": 114,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0849",
        "x": 1803,
        "y": 119,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0850",
        "x": 1193,
        "y": 237,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0851",
        "x": 1824,
        "y": 128,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0852",
        "x": 1416,
        "y": 175,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0853",
        "x": 2861,
        "y": 100,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0854",
        "x": 565,
        "y": 355,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0855",
        "x": 2216,
        "y": 363,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0856",
        "x": 1196,
        "y": 75,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0857",
        "x": 1665,
        "y": 74,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0858",
        "x": 1754,
        "y": 151,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0859",
        "x": 2973,
        "y": 170,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0860",
        "x": 2205,
        "y": 93,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0861",
        "x": 1711,
        "y": 241,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0862",
        "x": 2037,
        "y": 82,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0863",
        "x": 855,
        "y": 213,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0864",
        "x": 3147,
        "y": 327,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0865",
        "x": 73,
        "y": 52,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0866",
        "x": 2331,
        "y": 194,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0867",
        "x": 3022,
        "y": 69,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0868",
        "x": 267,
        "y": 368,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0869",
        "x": 1698,
        "y": 233,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0870",
        "x": 1019,
        "y": 228,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0871",
        "x": 1559,
        "y": 314,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0872",
        "x": 1100,
        "y": 380,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0873",
        "x": 1352,
        "y": 398,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0874",
        "x": 79,
        "y": 28,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0875",
        "x": 1924,
        "y": 53,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0876",
        "x": 2521,
        "y": 371,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0877",
        "x": 1069,
        "y": 328,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0878",
        "x": 107,
        "y": 378,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0879",
        "x": 1871,
        "y": 406,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0880",
        "x": 141,
        "y": 162,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0881",
        "x": 1392,
        "y": 18,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0882",
        "x": 3197,
        "y": 246,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0883",
        "x": 2033,
        "y": 268,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0884",
        "x": 1567,
        "y": 62,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0885",
        "x": 474,
        "y": 369,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0886",
        "x": 2097,
        "y": 77,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0887",
        "x": 1689,
        "y": 338,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0888",
        "x": 2862,
        "y": 93,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0889",
        "x": 2510,
        "y": 236,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0890",
        "x": 1908,
        "y": 111,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0891",
        "x": 1609,
        "y": 130,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0892",
        "x": 2985,
        "y": 11,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0893",
        "x": 47,
        "y": 367,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0894",
        "x": 2706,
        "y": 401,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0895",
        "x": 2875,
        "y": 139,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0896",
        "x": 1978,
        "y": 64,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0897",
        "x": 181,
        "y": 311,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0898",
        "x": 2848,
        "y": 259,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0899",
        "x": 671,
        "y": 52,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0900",
        "x": 760,
        "y": 335,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0901",
        "x": 1492,
        "y": 70,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0902",
        "x": 481,
        "y": 181,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0903",
        "x": 1930,
        "y": 99,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0904",
        "x": 838,
        "y": 267,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0905",
        "x": 1945,
        "y": 378,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0906",
        "x": 436,
        "y": 208,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0907",
        "x": 2028,
        "y": 313,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0908",
        "x": 2203,
        "y": 272,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0909",
        "x": 992,
        "y": 312,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0910",
        "x": 1597,
        "y": 367,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0911",
        "x": 415,
        "y": 240,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0912",
        "x": 1689,
        "y": 271,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0913",
        "x": 2795,
        "y": 249,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0914",
        "x": 2915,
        "y": 111,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0915",
        "x": 2855,
        "y": 18,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0916",
        "x": 1724,
        "y": 137,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0917",
        "x": 3014,
        "y": 48,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0918",
        "x": 1296,
        "y": 73,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0919",
        "x": 1445,
        "y": 10,
        "brightness": 1,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0920",
        "x": 1927,
        "y": 268,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0921",
        "x": 2888,
        "y": 31,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0922",
        "x": 2004,
        "y": 206,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0923",
        "x": 2833,
        "y": 136,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0924",
        "x": 2561,
        "y": 356,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0925",
        "x": 2567,
        "y": 143,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0926",
        "x": 348,
        "y": 388,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0927",
        "x": 161,
        "y": 144,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0928",
        "x": 2073,
        "y": 353,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0929",
        "x": 918,
        "y": 386,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0930",
        "x": 2846,
        "y": 52,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0931",
        "x": 123,
        "y": 267,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0932",
        "x": 2594,
        "y": 183,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0933",
        "x": 214,
        "y": 158,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0934",
        "x": 1139,
        "y": 76,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0935",
        "x": 943,
        "y": 429,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0936",
        "x": 3187,
        "y": 385,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0937",
        "x": 795,
        "y": 387,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0938",
        "x": 264,
        "y": 401,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0939",
        "x": 2879,
        "y": 165,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0940",
        "x": 2184,
        "y": 356,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0941",
        "x": 299,
        "y": 62,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0942",
        "x": 1264,
        "y": 119,
        "brightness": 2,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0943",
        "x": 2606,
        "y": 260,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0944",
        "x": 899,
        "y": 409,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0945",
        "x": 2018,
        "y": 254,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0946",
        "x": 2721,
        "y": 328,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0947",
        "x": 2670,
        "y": 220,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0948",
        "x": 54,
        "y": 249,
        "brightness": 4,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0949",
        "x": 336,
        "y": 39,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0950",
        "x": 687,
        "y": 215,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0951",
        "x": 2609,
        "y": 254,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0952",
        "x": 2066,
        "y": 141,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0953",
        "x": 968,
        "y": 344,
        "brightness": 2,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0954",
        "x": 2515,
        "y": 402,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0955",
        "x": 1963,
        "y": 348,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0956",
        "x": 873,
        "y": 249,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0957",
        "x": 966,
        "y": 280,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0958",
        "x": 1301,
        "y": 166,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0959",
        "x": 891,
        "y": 91,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0960",
        "x": 2758,
        "y": 149,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0961",
        "x": 2754,
        "y": 282,
        "brightness": 3,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0962",
        "x": 927,
        "y": 287,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0963",
        "x": 2195,
        "y": 249,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0964",
        "x": 1334,
        "y": 128,
        "brightness": 3,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0965",
        "x": 538,
        "y": 292,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0966",
        "x": 3131,
        "y": 293,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0967",
        "x": 2946,
        "y": 267,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0968",
        "x": 1329,
        "y": 73,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0969",
        "x": 1222,
        "y": 72,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0970",
        "x": 2152,
        "y": 199,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0971",
        "x": 3026,
        "y": 78,
        "brightness": 2,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0972",
        "x": 318,
        "y": 182,
        "brightness": 4,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0973",
        "x": 188,
        "y": 293,
        "brightness": 3,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0974",
        "x": 1891,
        "y": 196,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0975",
        "x": 2979,
        "y": 289,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0976",
        "x": 2293,
        "y": 246,
        "brightness": 4,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0977",
        "x": 1277,
        "y": 66,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0978",
        "x": 2873,
        "y": 278,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0979",
        "x": 1111,
        "y": 190,
        "brightness": 2,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0980",
        "x": 1185,
        "y": 199,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0981",
        "x": 1824,
        "y": 170,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0982",
        "x": 3164,
        "y": 83,
        "brightness": 3,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0983",
        "x": 476,
        "y": 150,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0984",
        "x": 2184,
        "y": 186,
        "brightness": 2,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0985",
        "x": 2847,
        "y": 54,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0986",
        "x": 2842,
        "y": 254,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0987",
        "x": 814,
        "y": 271,
        "brightness": 1,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0988",
        "x": 635,
        "y": 147,
        "brightness": 1,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0989",
        "x": 1542,
        "y": 66,
        "brightness": 1,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0990",
        "x": 2467,
        "y": 386,
        "brightness": 4,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0991",
        "x": 1576,
        "y": 49,
        "brightness": 4,
        "color": "#b7d4ff"
    },
    {
        "id": "NAV-0992",
        "x": 547,
        "y": 85,
        "brightness": 3,
        "color": "#d7e7ff"
    },
    {
        "id": "NAV-0993",
        "x": 1587,
        "y": 295,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0994",
        "x": 2297,
        "y": 130,
        "brightness": 4,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0995",
        "x": 2059,
        "y": 315,
        "brightness": 1,
        "color": "#f5e0bd"
    },
    {
        "id": "NAV-0996",
        "x": 2635,
        "y": 316,
        "brightness": 3,
        "color": "#c7e5ff"
    },
    {
        "id": "NAV-0997",
        "x": 3093,
        "y": 181,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-0998",
        "x": 2520,
        "y": 137,
        "brightness": 2,
        "color": "#fff3de"
    },
    {
        "id": "NAV-0999",
        "x": 2415,
        "y": 211,
        "brightness": 1,
        "color": "#91c9ff"
    },
    {
        "id": "NAV-1000",
        "x": 1714,
        "y": 251,
        "brightness": 1,
        "color": "#d7e7ff"
    },
]

@app.get("/")
def index():
    return render_template_string(PAGE)

@app.get("/health")
def health():
    return jsonify({"status": "ok", "game": "Lunar Path", "atlas_points": len(SPACE_ATLAS)})

@app.get("/api/atlas")
def atlas():
    return jsonify({"width": 3200, "height": 430, "stars": SPACE_ATLAS})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False)

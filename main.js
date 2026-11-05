import * as THREE from "three";
import "./style.css";
const root=document.querySelector("#game"),scene=new THREE.Scene();
scene.background=new THREE.Color(0x07111e);scene.fog=new THREE.Fog(0x07111e,18,55);
const camera=new THREE.PerspectiveCamera(74,innerWidth/innerHeight,.1,100);camera.position.set(0,1.7,13);
const renderer=new THREE.WebGLRenderer({antialias:true});renderer.setSize(innerWidth,innerHeight);renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.shadowMap.enabled=true;renderer.outputColorSpace=THREE.SRGBColorSpace;root.append(renderer.domElement);
scene.add(new THREE.HemisphereLight(0xc6e0ff,0x263342,1.8));
const sun=new THREE.DirectionalLight(0xffe0c0,2.3);sun.position.set(-7,14,8);sun.castShadow=true;scene.add(sun);
const mat=(c,metal=0,rough=.7,em=0)=>new THREE.MeshStandardMaterial({color:c,metalness:metal,roughness:rough,emissive:em});
const M={floor:mat(0x192a3b),wall:mat(0x263b4f),dark:mat(0x0b1724,.3),white:mat(0xe1e7e9),orange:mat(0xf28b45,.2),glass:mat(0x27617a,.4,.2),cyan:mat(0x267c8d,.2,.3,0x12434b),green:mat(0x55cc91,0,0.4,0x16452d)};
function cube(x,y,z,a,b,c,m){let o=new THREE.Mesh(new THREE.BoxGeometry(a,b,c),m);o.position.set(x,y,z);o.castShadow=true;o.receiveShadow=true;scene.add(o);return o}
function cyl(x,y,z,r1,r2,h,m,n=20){let o=new THREE.Mesh(new THREE.CylinderGeometry(r1,r2,h,n),m);o.position.set(x,y,z);o.castShadow=true;scene.add(o);return o}
function ball(x,y,z,r,m){let o=new THREE.Mesh(new THREE.SphereGeometry(r,20,14),m);o.position.set(x,y,z);o.castShadow=true;scene.add(o);return o}
function sign(t,x,y,z){let c=document.createElement("canvas");c.width=512;c.height=128;let g=c.getContext("2d");g.fillStyle="#091725";g.fillRect(0,0,512,128);g.strokeStyle="#f28b45";g.lineWidth=5;g.strokeRect(5,5,502,118);g.fillStyle="#e9f0f5";g.font="bold 32px Arial";g.textAlign="center";g.fillText(t,256,77);let s=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(c)}));s.position.set(x,y,z);s.scale.set(3.7,.9,1);scene.add(s)}
// Hangar shell and lit floor grid
cube(0,4,-20,42,8,.7,M.wall);cube(-21,4,0,.7,8,40,M.wall);cube(21,4,0,.7,8,40,M.wall);cube(-15,4,20,12,8,.7,M.wall);cube(15,4,20,12,8,.7,M.wall);cube(0,7.8,0,42,.3,40,M.dark);
let floor=new THREE.Mesh(new THREE.PlaneGeometry(42,40),M.floor);floor.rotation.x=-Math.PI/2;floor.receiveShadow=true;scene.add(floor);
for(let x=-18;x<=18;x+=6){cube(x,7.55,-1,.16,.06,30,M.cyan);cube(x,.015,0,.035,.02,38,M.cyan)}
// Observation windows, stars, moon
for(let x of [-14,-7,0,7,14]){cube(x,4.5,-19.55,5.3,3.4,.2,M.dark);cube(x,4.5,-19.4,5,3.1,.08,M.glass)}
for(let i=0;i<65;i++)ball((Math.random()-.5)*38,3+Math.random()*4,-19.25,.035,mat(0xe8f3ff,0,1,0x7d91aa));
let moon=ball(12,4.8,-19.1,1.25,mat(0xaebbc3));moon.scale.set(1.3,1,.18);
// Saturn V display
cyl(-12,2.5,-8,.45,.62,4.4,M.white);cyl(-12,4.9,-8,.37,.45,1,M.orange);cyl(-12,5.7,-8,.26,.37,.8,M.white);
let nose=new THREE.Mesh(new THREE.ConeGeometry(.27,.9,20),M.white);nose.position.set(-12,6.55,-8);scene.add(nose);
for(let a=0;a<4;a++){let f=cube(-12+Math.sin(a*Math.PI/2)*.48,.55,-8+Math.cos(a*Math.PI/2)*.48,.22,.9,.65,M.orange);f.rotation.y=a*Math.PI/2}
sign("SATURN V DISPLAY",-12,7.8,-8);
// Spacesuit mannequin
cyl(-7,1.4,2,.48,.55,1.3,M.white);ball(-7,2.35,2,.42,M.white);ball(-7,2.35,2.36,.29,M.glass);cube(-7,1.5,1.5,.65,1.1,.35,M.dark);cyl(-7.6,1.35,2,.16,.18,1,M.white);cyl(-6.4,1.35,2,.16,.18,1,M.white);cube(-7,.15,2,1.6,.3,1.5,M.dark);sign("SUIT & LIFE SUPPORT",-7,3.3,2);
// Lunar module mock-up
cyl(8,2.8,-7,1.15,1.25,1.2,M.orange,6);let cabin=new THREE.Mesh(new THREE.ConeGeometry(1.3,1.2,6),M.white);cabin.position.set(8,3.9,-7);scene.add(cabin);
for(let a=0;a<4;a++){let an=a*Math.PI/2+.78;let leg=cube(8+Math.sin(an)*1.35,1,-7+Math.cos(an)*1.35,.13,2,.13,M.white);leg.rotation.z=-Math.sin(an)*.28;cube(8+Math.sin(an)*1.65,.08,-7+Math.cos(an)*1.65,.65,.12,.55,M.dark)}
sign("LUNAR MODULE / EAGLE",8,5.3,-7);
// Flight-control desks and monitors
cube(8,1.1,5,5.8,1.2,1.5,M.dark);
for(let x of [6.1,8,9.9]){cube(x,2.25,4.58,1.55,1.25,.16,M.dark);cube(x,2.25,4.69,1.35,1.05,.04,M.cyan);for(let j=0;j<3;j++)cube(x,2.5-j*.22,4.72,.8-j*.13,.025,.02,M.green)}
sign("FLIGHT CONTROL SIMULATOR",8,3.25,5);
// Lunar rover
cube(-1,.85,-7,2.4,.35,1.25,M.orange);for(let x of [-1.9,-.1])for(let z of [-7.8,-6.2]){let w=cyl(x,.45,z,.42,.42,.2,M.dark,16);w.rotation.z=Math.PI/2}cube(-1,1.35,-7.15,.65,.7,.6,M.white);sign("LUNAR SURFACE OPS",-1,2.4,-7);
// Wall labels
for(let [x,t] of [[-15,"MISSION BRIEFING"],[-5,"SPACECRAFT SYSTEMS"],[5,"FLIGHT OPERATIONS"],[15,"CREW RECOVERY"]])sign(t,x,6.4,-19.05);
const stations=[
{id:"suit",title:"Astronaut suit & life support",x:-7,z:2,r:3.1,task:"Inspect the spacesuit",desc:"Spacesuits help protect astronauts and provide oxygen, pressure, cooling, and communications. You inspected the suit and life-support display."},
{id:"rocket",title:"Saturn V launch systems",x:-12,z:-8,r:3.4,task:"Study the Saturn V",desc:"The Saturn V was a three-stage launch vehicle. Its stages provided the thrust needed to carry Apollo toward Earth orbit and onward to the Moon."},
{id:"lunar",title:"Lunar Module — Eagle",x:8,z:-7,r:3.5,task:"Inspect the Lunar Module",desc:"Eagle had a descent stage for landing and an ascent stage that returned Armstrong and Aldrin to lunar orbit."},
{id:"cockpit",title:"Flight control simulator",x:8,z:5,r:3.5,task:"Run the flight-control exercise",desc:"Mission Control monitored spacecraft status, navigation, and communications. Complete the decision check below."},
{id:"rover",title:"Lunar surface operations",x:-1,z:-7,r:3.2,task:"Explore lunar surface operations",desc:"Apollo 11 surface activity included collecting samples, documenting the landing site, and deploying scientific experiments."}
];
let done=new Set(JSON.parse(localStorage.apolloStations||"[]")),score=+(localStorage.apolloGameScore||0),markers=[];
for(let s of stations){let ring=new THREE.Mesh(new THREE.TorusGeometry(.72,.055,8,36),new THREE.MeshBasicMaterial({color:done.has(s.id)?0x55cc91:0xf28b45}));ring.rotation.x=Math.PI/2;ring.position.set(s.x,.09,s.z);scene.add(ring);let light=new THREE.PointLight(done.has(s.id)?0x55cc91:0xf28b45,1.4,4);light.position.set(s.x,1.2,s.z);scene.add(light);markers.push({s,ring,light})}
const hud=document.createElement("div");hud.className="hud";hud.innerHTML=`<div class="brand"><b>APOLLO 11</b><small>ASTRONAUT ACADEMY</small></div><div class="stats">TRAINING XP <b id="xp">${score}</b>　 STATIONS <b id="count">${done.size}/5</b></div><div class="assignment"><small>CURRENT ASSIGNMENT</small><b id="task"></b><span>Find a glowing station and press E.</span></div><div class="cross">+</div><div class="prompt" id="prompt"></div><div class="controls">WASD WALK　·　MOUSE LOOK　·　E INTERACT　·　ESC RELEASE</div>`;root.append(hud);
const intro=document.createElement("div");intro.className="overlay";intro.innerHTML=`<section class="welcome"><label>NASA / APOLLO PROGRAM · TRAINING FACILITY</label><div class="seal">A11</div><h1>ASTRONAUT<br><em>TRAINING CENTER</em></h1><p>This is a walkable 3D training facility. Explore the hangar, approach spacecraft and equipment, and interact with training stations.</p><div class="keys"><span>W A S D <small>WALK</small></span><span>MOUSE <small>LOOK</small></span><span>E <small>INTERACT</small></span></div><button id="enter">ENTER FACILITY ↗</button><small class="note">EDUCATIONAL GAME · NOT A REAL FLIGHT SYSTEM</small></section>`;root.append(intro);
const modal=document.createElement("div");modal.className="modal hidden";root.append(modal);
function refresh(){document.querySelector("#xp").textContent=score;document.querySelector("#count").textContent=stations.filter(s=>done.has(s.id)).length+"/5";let next=stations.find(s=>!done.has(s.id));document.querySelector("#task").textContent=next?next.task:"All training stations completed!"}
function close(){modal.classList.add("hidden")}
function interact(s){modal.classList.remove("hidden");modal.innerHTML=`<section class="dialog"><button class="close">×</button><label>TRAINING STATION / ${done.has(s.id)?"REVIEW":"NEW EXERCISE"}</label><h2>${s.title}</h2><p>${s.desc}</p><div class="objective"><small>TRAINING OBJECTIVE</small><b>${s.task}</b></div>${s.id==="cockpit"?`<div class="question"><b>FLIGHT DIRECTOR CHECK</b><p>Before a mission phase proceeds, what should the team do?</p><button data-a="0">A · Skip the checklist</button><button data-a="1">B · Verify systems and confirm go/no-go</button><button data-a="2">C · Ignore status reports</button><div id="answer"></div></div>`:""}<button class="finish">${done.has(s.id)?"CLOSE BRIEFING":"COMPLETE TRAINING +50 XP"}</button></section>`;
modal.querySelector(".close").onclick=close;modal.querySelector(".finish").onclick=()=>{if(!done.has(s.id)){done.add(s.id);score+=50;save()}close();refresh();updateMarkers()};
modal.querySelectorAll("[data-a]").forEach(b=>b.onclick=()=>{let good=b.dataset.a==="1";document.querySelector("#answer").innerHTML=good?"<b class='good'>CORRECT · +25 XP</b><p>Verify the checklist and confirm the team's go/no-go.</p>":"<b class='bad'>NOT QUITE</b><p>Teams verify systems and confirm go/no-go before proceeding.</p>";if(good&&!done.has("cockpitQuiz")){done.add("cockpitQuiz");score+=25;save();refresh()}})}
function save(){localStorage.apolloStations=JSON.stringify([...done]);localStorage.apolloGameScore=String(score)}
function updateMarkers(){for(let m of markers){let d=done.has(m.s.id);m.ring.material.color.set(d?0x55cc91:0xf28b45);m.light.color.set(d?0x55cc91:0xf28b45)}}
refresh();
let yaw=0,pitch=0,locked=false,current=null,last=performance.now(),keys={};
document.querySelector("#enter").onclick=()=>{intro.classList.add("hidden");renderer.domElement.requestPointerLock()};
renderer.domElement.addEventListener("click",()=>{if(intro.classList.contains("hidden")&&modal.classList.contains("hidden")&&!locked)renderer.domElement.requestPointerLock()});
document.addEventListener("pointerlockchange",()=>locked=document.pointerLockElement===renderer.domElement);
document.addEventListener("mousemove",e=>{if(!locked||!modal.classList.contains("hidden"))return;yaw-=e.movementX*.0022;pitch=Math.max(-1.05,Math.min(1.05,pitch-e.movementY*.0018))});
document.addEventListener("keydown",e=>{keys[e.code]=true;if(["ArrowUp","ArrowDown","ArrowLeft","ArrowRight","Space"].includes(e.code))e.preventDefault();if(e.code==="KeyE"&&current&&modal.classList.contains("hidden"))interact(current);if(e.code==="Escape"&&!modal.classList.contains("hidden"))close()});
document.addEventListener("keyup",e=>keys[e.code]=false);
const obstacles=[{x:-12,z:-8,r:1.45},{x:-7,z:2,r:.8},{x:8,z:-7,r:1.65},{x:8,z:5,r:2.2},{x:-1,z:-7,r:1.5}];
function move(dt){if(!locked||!modal.classList.contains("hidden"))return;let f=new THREE.Vector3(-Math.sin(yaw),0,-Math.cos(yaw)),r=new THREE.Vector3(Math.cos(yaw),0,-Math.sin(yaw)),v=new THREE.Vector3();if(keys.KeyW||keys.ArrowUp)v.add(f);if(keys.KeyS||keys.ArrowDown)v.sub(f);if(keys.KeyD||keys.ArrowRight)v.add(r);if(keys.KeyA||keys.ArrowLeft)v.sub(r);if(v.lengthSq()){v.normalize().multiplyScalar(5*dt);let nx=THREE.MathUtils.clamp(camera.position.x+v.x,-19,19),nz=THREE.MathUtils.clamp(camera.position.z+v.z,-18.5,18.5);if(!obstacles.some(o=>Math.hypot(nx-o.x,nz-o.z)<o.r)){camera.position.x=nx;camera.position.z=nz}}camera.position.y=1.7;camera.rotation.order="YXZ";camera.rotation.y=yaw;camera.rotation.x=pitch}
function loop(t){requestAnimationFrame(loop);let dt=Math.min((t-last)/1000,.04);last=t;move(dt);current=null;let dmin=99;for(let s of stations){let d=Math.hypot(camera.position.x-s.x,camera.position.z-s.z);if(d<s.r&&d<dmin){dmin=d;current=s}}let prompt=document.querySelector("#prompt");prompt.style.display=current&&locked?"block":"none";if(current)prompt.textContent="E · INTERACT — "+current.title.toUpperCase();for(let m of markers)m.ring.rotation.z+=dt*.4;renderer.render(scene,camera)}
requestAnimationFrame(loop);
addEventListener("resize",()=>{camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight)});

import './style.css';

const events = [
  {
    id: 'launch', day: 'JUL 16', time: '13:32:00 UTC', elapsed: 'T+00:00',
    phase: 'EARTH DEPARTURE', title: 'Liftoff from Kennedy Space Center',
    summary: 'The 363-foot Saturn V launches from Launch Complex 39A, carrying Armstrong, Collins, and Aldrin toward Earth orbit.',
    detail: 'The five F-1 engines of the S-IC first stage ignite, producing the thrust needed to lift the vehicle from the pad. Apollo 11 begins its journey at 13:32 UTC on July 16, 1969.',
    facts: [['Launch vehicle','Saturn V'],['Launch site','LC-39A · Kennedy Space Center'],['Crew','Armstrong · Collins · Aldrin']]
  },
  {
    id: 'orbit', day: 'JUL 16', time: '13:44 UTC · approx.', elapsed: 'T+00:12',
    phase: 'EARTH ORBIT', title: 'Earth parking orbit',
    summary: 'The first and second stages separate. The spacecraft reaches Earth orbit roughly twelve minutes after liftoff.',
    detail: 'After the S-IC and S-II stages complete their work, the S-IVB third stage places the spacecraft into a temporary parking orbit around Earth.',
    facts: [['Orbit','Earth parking orbit'],['Vehicle','S-IVB + spacecraft'],['Next move','Trans-lunar injection']]
  },
  {
    id: 'tli', day: 'JUL 16', time: '16:22 UTC · approx.', elapsed: 'T+02:50',
    phase: 'TRANS-LUNAR INJECTION', title: 'The Moon becomes the destination',
    summary: 'The S-IVB reignites and accelerates Apollo 11 out of Earth orbit onto its translunar trajectory.',
    detail: 'After approximately one and a half Earth orbits, the Saturn V third stage fires again. This Trans-Lunar Injection burn sends the spacecraft toward the Moon.',
    facts: [['Maneuver','Trans-Lunar Injection'],['Engine','J-2 · S-IVB'],['Destination','Lunar orbit']]
  },
  {
    id: 'dock', day: 'JUL 16', time: '17:00 UTC · approx.', elapsed: 'T+03:28',
    phase: 'SPACECRAFT CONFIGURATION', title: 'Columbia meets Eagle',
    summary: 'The Command and Service Module turns around, docks with the Lunar Module, and extracts Eagle from the Saturn V adapter.',
    detail: 'The Command and Service Module (CSM) separates, performs a transposition maneuver, docks nose-first with the Lunar Module (LM), and pulls Eagle away from the spent launch vehicle.',
    facts: [['Command module','Columbia'],['Lunar module','Eagle'],['Crew configuration','Three aboard CSM']]
  },
  {
    id: 'coast', day: 'JUL 17–18', time: '3-day translunar coast', elapsed: 'T+1–2 DAYS',
    phase: 'LUNAR TRANSIT', title: 'Three days across the void',
    summary: 'The combined spacecraft coasts through space toward the Moon while the crew monitors systems and makes course corrections.',
    detail: 'During the translunar coast, the crew checks spacecraft systems, navigates, and prepares for lunar orbit insertion and the landing operations ahead.',
    facts: [['Spacecraft','CSM Columbia + LM Eagle'],['Journey','Earth to Moon'],['Crew activity','Navigation and system checks']]
  },
  {
    id: 'loi', day: 'JUL 19', time: '17:21 UTC · approx.', elapsed: 'T+3 DAYS',
    phase: 'LUNAR ORBIT', title: 'Captured by the Moon',
    summary: 'The Service Module engine slows the spacecraft, allowing the Moon’s gravity to capture Apollo 11 into lunar orbit.',
    detail: 'The Lunar Orbit Insertion burn places Apollo 11 into orbit around the Moon. The crew observes the lunar surface and prepares for the descent to the Sea of Tranquility.',
    facts: [['Maneuver','Lunar Orbit Insertion'],['Engine','Service Propulsion System'],['Destination','Lunar orbit']]
  },
  {
    id: 'separation', day: 'JUL 20', time: '17:44 UTC · approx.', elapsed: 'T+4 DAYS',
    phase: 'LUNAR MODULE DESCENT', title: 'Eagle separates from Columbia',
    summary: 'Armstrong and Aldrin descend in Eagle. Collins remains alone aboard Columbia in lunar orbit.',
    detail: 'The two spacecraft separate. Collins continues orbiting the Moon in Columbia while Armstrong and Aldrin prepare Eagle for powered descent.',
    facts: [['Eagle crew','Armstrong · Aldrin'],['Columbia pilot','Michael Collins'],['Landing region','Sea of Tranquility']]
  },
  {
    id: 'landing', day: 'JUL 20', time: '20:17:40 UTC', elapsed: 'T+4D 06H 45M',
    phase: 'LUNAR LANDING', title: 'Tranquility Base',
    summary: 'Eagle touches down on the Moon. Armstrong reports: “The Eagle has landed.”',
    detail: 'During powered descent, computer alarms appear and the crew sees a boulder field near the planned landing point. Armstrong takes manual control and guides Eagle to a safe landing with a small fuel reserve remaining.',
    facts: [['Landing site','Sea of Tranquility'],['Spacecraft','Lunar Module Eagle'],['Landing time','20:17:40 UTC']]
  },
  {
    id: 'eva', day: 'JUL 21', time: '02:56 UTC', elapsed: 'T+5 DAYS',
    phase: 'EXTRAVEHICULAR ACTIVITY', title: 'First steps on another world',
    summary: 'Armstrong steps onto the lunar surface, followed shortly by Aldrin. The crew deploys experiments and collects samples.',
    detail: 'The astronauts photograph the landing site, deploy scientific equipment, plant the U.S. flag, and collect approximately 21.6 kg of lunar rocks and soil. The surface EVA lasts about two and a half hours.',
    facts: [['EVA start','02:56 UTC · July 21'],['Samples','21.6 kg approx.'],['Surface activity','Experiments · photos · sample collection']]
  },
  {
    id: 'ascent', day: 'JUL 21', time: '17:54 UTC · approx.', elapsed: 'T+5 DAYS',
    phase: 'LUNAR ASCENT', title: 'Eagle lifts off',
    summary: 'The Lunar Module ascent stage launches from the Moon, leaving the descent stage at Tranquility Base.',
    detail: 'The ascent engine fires and carries Armstrong and Aldrin back into lunar orbit. The descent stage remains on the surface as the launch platform.',
    facts: [['Vehicle','Eagle ascent stage'],['Crew','Armstrong · Aldrin'],['Left behind','Descent stage']]
  },
  {
    id: 'rendezvous', day: 'JUL 21', time: '21:35 UTC · approx.', elapsed: 'T+5 DAYS',
    phase: 'RENDEZVOUS & DOCKING', title: 'Reunited with Columbia',
    summary: 'Eagle rendezvous and docks with Columbia. The astronauts and lunar samples transfer back to the Command Module.',
    detail: 'Collins has kept Columbia in lunar orbit. After docking, Armstrong and Aldrin transfer into the Command Module with the collected samples and film. Eagle’s ascent stage is later jettisoned.',
    facts: [['Docking partner','CSM Columbia'],['Command Module pilot','Michael Collins'],['Cargo','Lunar samples and film']]
  },
  {
    id: 'tei', day: 'JUL 22', time: '04:55 UTC · approx.', elapsed: 'T+6 DAYS',
    phase: 'RETURN TO EARTH', title: 'Leaving lunar orbit',
    summary: 'Columbia fires its Service Module engine for Trans-Earth Injection and begins the journey home.',
    detail: 'The Trans-Earth Injection maneuver places the spacecraft on a trajectory back to Earth. The crew spends the next few days crossing the distance between the Moon and home.',
    facts: [['Maneuver','Trans-Earth Injection'],['Spacecraft','Columbia'],['Journey','Moon to Earth']]
  },
  {
    id: 'entry', day: 'JUL 24', time: '16:21 UTC · approx.', elapsed: 'T+8 DAYS',
    phase: 'ATMOSPHERIC ENTRY', title: 'A fiery return',
    summary: 'The Service Module is jettisoned. The Command Module enters Earth’s atmosphere behind its heat shield.',
    detail: 'Only the cone-shaped Command Module continues toward Earth. Its heat shield protects the crew during high-speed atmospheric entry. Drogue and main parachutes slow the capsule for recovery.',
    facts: [['Returning craft','Command Module Columbia'],['Protection','Ablative heat shield'],['Recovery system','Drogue + main parachutes']]
  },
  {
    id: 'splashdown', day: 'JUL 24', time: '16:50:35 UTC', elapsed: 'T+8D 03H 18M',
    phase: 'MISSION COMPLETE', title: 'Splashdown in the Pacific',
    summary: 'Columbia lands safely in the Pacific Ocean. The crew is recovered by USS Hornet.',
    detail: 'Apollo 11 completes its historic mission after 8 days, 3 hours, 18 minutes, and 35 seconds. The astronauts are recovered by the aircraft carrier USS Hornet and enter a 21-day quarantine protocol.',
    facts: [['Recovery area','Pacific Ocean'],['Recovery ship','USS Hornet'],['Mission duration','8d 03h 18m 35s']]
  }
];

const app = document.querySelector('#app');
let active = 0;
let clockMode = 'mission';
let clockTimer = null;
let elapsedSeconds = 0;
let running = false;

const icon = (name) => {
  const paths = {
    arrow: '<path d="M5 12h14M13 6l6 6-6 6"/>',
    play: '<path d="m8 5 12 7-12 7z" fill="currentColor" stroke="none"/>',
    pause: '<path d="M8 5h3v14H8zM15 5h3v14h-3z" fill="currentColor" stroke="none"/>',
    chevron: '<path d="m9 18 6-6-6-6"/>',
    orbit: '<ellipse cx="12" cy="12" rx="9" ry="4.5" transform="rotate(-32 12 12)"/><circle cx="12" cy="12" r="2"/>',
    radio: '<path d="M4 9a12 12 0 0 1 16 0M7 12a7.5 7.5 0 0 1 10 0m-7 3a3 3 0 0 1 4 0"/><circle cx="12" cy="18" r="1"/>',
    crosshair: '<circle cx="12" cy="12" r="8"/><path d="M12 2v4m0 12v4M2 12h4m12 0h4"/>'
  };
  return `<svg viewBox="0 0 24 24" aria-hidden="true">${paths[name] || ''}</svg>`;
};

function render() {
  app.innerHTML = `
    <div class="grain"></div>
    <header class="topbar">
      <a class="brand" href="#top" aria-label="Apollo 11 home">
        <span class="brand-mark">A<span>11</span></span>
        <span class="brand-copy"><b>APOLLO 11</b><small>MISSION CONTROL</small></span>
      </a>
      <nav class="top-nav"><a class="active" href="#mission">MISSION</a><a href="#timeline">TIMELINE</a><a href="#spacecraft">SPACECRAFT</a></nav>
      <div class="top-status"><i></i><span>ARCHIVE MODE</span><span class="utc">UTC</span></div>
    </header>

    <main id="top">
      <section class="hero">
        <div class="hero-copy">
          <div class="eyebrow"><span class="eyebrow-line"></span> NASA · AS-506 · JULY 1969</div>
          <h1>ONE GIANT<br><em>LEAP.</em></h1>
          <p class="hero-intro">The complete journey of Apollo 11 — from the thunder of Saturn V to the quiet of the Pacific Ocean.</p>
          <div class="hero-actions">
            <a class="primary-btn" href="#timeline">EXPLORE THE MISSION ${icon('arrow')}</a>
            <button class="text-btn" id="jumpLaunch">START AT LIFTOFF <span>↗</span></button>
          </div>
          <div class="hero-meta">
            <div><small>MISSION DURATION</small><b>8D 03H 18M 35S</b></div>
            <div><small>CREW</small><b>ARMSTRONG · COLLINS · ALDRIN</b></div>
          </div>
        </div>
        <div class="hero-art" aria-label="Illustration of Saturn V rising toward the Moon">
          <div class="art-coordinate">28°36' N<br>80°36' W</div>
          <div class="moon-orb"></div>
          <div class="orbit orbit-one"></div><div class="orbit orbit-two"></div>
          <div class="stars"></div>
          <div class="rocket-glow"></div>
          <svg class="saturn" viewBox="0 0 240 600" role="img" aria-label="Saturn V rocket illustration">
            <defs>
              <linearGradient id="rocketBody" x1="0" x2="1"><stop stop-color="#9da8ad"/><stop offset=".45" stop-color="#f0eee5"/><stop offset="1" stop-color="#77858c"/></linearGradient>
              <linearGradient id="flame" x1="0" x2="0" y1="0" y2="1"><stop stop-color="#fff4be"/><stop offset=".35" stop-color="#f6a54d"/><stop offset="1" stop-color="#e45b2e" stop-opacity="0"/></linearGradient>
            </defs>
            <path d="M120 20 L143 92 L143 430 L97 430 L97 92 Z" fill="url(#rocketBody)" stroke="#e9e7de" stroke-width="2"/>
            <path d="M120 20 L143 92 L97 92 Z" fill="#d9d8cf"/>
            <path d="M97 115h46v18H97z" fill="#c64f3e"/>
            <path d="M97 150h46v9H97z" fill="#202d37"/>
            <path d="M97 185h46v12H97z" fill="#c64f3e"/>
            <path d="M97 232h46v14H97z" fill="#202d37"/>
            <path d="M97 290h46v12H97z" fill="#c64f3e"/>
            <path d="M97 345h46v12H97z" fill="#202d37"/>
            <path d="M97 395h46v35H97z" fill="#c64f3e"/>
            <path d="M97 405L64 475h33l23-40 23 40h33l-33-70z" fill="#aeb7b9"/>
            <path d="M104 430 Q90 520 112 586 Q120 602 128 586 Q150 520 136 430Z" fill="url(#flame)"/>
            <path d="M112 438 Q107 505 120 548 Q133 505 128 438Z" fill="#fff0b4" opacity=".8"/>
            <path d="M115 75h10v28h-10z" fill="#687985"/>
          </svg>
          <div class="art-caption"><span>01 / 15</span><b>THE JOURNEY BEGINS</b><span>KENNEDY SPACE CENTER</span></div>
          <div class="art-vertical">SATURN V · APOLLO 11</div>
        </div>
        <div class="hero-bottomline"><span>SCROLL TO BEGIN</span><span class="scroll-mark"></span><span>THE 1969 LUNAR MISSION</span></div>
      </section>

      <section class="mission-strip" id="mission">
        <div class="strip-heading"><span class="section-index">01</span><span>MISSION OVERVIEW</span></div>
        <div class="strip-grid">
          <div class="stat"><small>LAUNCH</small><b>16 <sup>JUL</sup> 1969</b><span>13:32:00 UTC</span></div>
          <div class="stat"><small>LUNAR LANDING</small><b>20 <sup>JUL</sup> 1969</b><span>20:17:40 UTC</span></div>
          <div class="stat"><small>SPLASHDOWN</small><b>24 <sup>JUL</sup> 1969</b><span>16:50:35 UTC</span></div>
          <div class="stat"><small>DESTINATION</small><b>THE MOON</b><span>SEA OF TRANQUILITY</span></div>
        </div>
      </section>

      <section class="mission-map-section">
        <div class="section-heading">
          <div><span class="section-index">02 / FLIGHT PATH</span><h2>Earth to <em>Moon.</em></h2></div>
          <p>A quarter-million miles from home.<br>One mission. Eight historic days.</p>
        </div>
        <div class="flight-map">
          <div class="map-grid"></div>
          <div class="map-label earth-label"><span class="planet earth"></span><b>EARTH</b><small>JUL 16 · 1969</small></div>
          <div class="map-label moon-label"><span class="planet moon"></span><b>THE MOON</b><small>JUL 19–21 · 1969</small></div>
          <svg class="flight-line" viewBox="0 0 1000 300" preserveAspectRatio="none" aria-label="Illustrated Apollo 11 flight path">
            <path class="path-shadow" d="M100 225 C300 15 650 15 890 225"/>
            <path class="path-main" d="M100 225 C300 15 650 15 890 225"/>
            <circle class="path-dot" r="5"><animateMotion dur="9s" repeatCount="indefinite" path="M100 225 C300 15 650 15 890 225"/></circle>
          </svg>
          <div class="map-callout callout-one"><span>01</span><b>TRANSLUNAR INJECTION</b><small>ESCAPE EARTH ORBIT</small></div>
          <div class="map-callout callout-two"><span>02</span><b>LUNAR ORBIT INSERTION</b><small>CAPTURED BY THE MOON</small></div>
          <div class="map-distance">≈ 384,400 KM <span>AVERAGE EARTH–MOON DISTANCE</span></div>
        </div>
      </section>

      <section class="timeline-section" id="timeline">
        <div class="section-heading">
          <div><span class="section-index">03 / THE MISSION LOG</span><h2>Every moment.<br><em>Every milestone.</em></h2></div>
          <p>Follow the mission from launch to recovery. Select any event to open its flight log.</p>
        </div>
        <div class="timeline-layout">
          <aside class="timeline-list">
            <div class="timeline-list-head"><span>FLIGHT LOG</span><span>15 EVENTS</span></div>
            <div id="eventList"></div>
          </aside>
          <article class="event-detail" id="eventDetail"></article>
        </div>
      </section>

      <section class="clock-section">
        <div class="clock-copy"><span class="section-index">04 / MISSION ELAPSED TIME</span><h2>Time is<br><em>history.</em></h2><p>Track the mission clock from liftoff. This interactive clock is a presentation timer, not a live historical telemetry feed.</p></div>
        <div class="clock-panel">
          <div class="clock-top"><span><i></i> MISSION CLOCK</span><span>AS-506 / CSM-107</span></div>
          <div class="clock-readout" id="clockReadout"><span>000</span><small>DAYS</small><span>00</span><small>HRS</small><span>00</span><small>MIN</small><span>00</span><small>SEC</small></div>
          <div class="clock-progress"><span id="clockProgress"></span></div>
          <div class="clock-controls"><button id="clockPlay">${icon('play')} START CLOCK</button><button id="clockReset">RESET</button><span id="clockState">READY · T+00:00:00</span></div>
        </div>
      </section>

      <section class="spacecraft-section" id="spacecraft">
        <div class="section-heading">
          <div><span class="section-index">05 / THE SPACECRAFT</span><h2>Three names.<br><em>One mission.</em></h2></div>
          <p>Each vehicle had a specific role in getting the crew to the Moon and safely home.</p>
        </div>
        <div class="craft-grid">
          <article class="craft-card">
            <div class="craft-art saturn-art"><div class="craft-number">01</div><svg viewBox="0 0 160 220"><path d="M80 8 96 45v120H64V45z" fill="#e7e4d9"/><path d="M64 60h32v9H64zm0 33h32v8H64zm0 34h32v8H64z" fill="#b94d3d"/><path d="m64 150-20 45h20l16-27 16 27h20l-20-45z" fill="#aeb6b8"/><path d="M70 164q-10 35 10 55 20-20 10-55" fill="#eea052"/></svg></div>
            <div class="craft-info"><span>LAUNCH VEHICLE</span><h3>Saturn V</h3><p>The three-stage rocket that delivered Apollo 11 from Kennedy Space Center into Earth orbit and onto its path to the Moon.</p><small>363 FT TALL · 3 STAGES</small></div>
          </article>
          <article class="craft-card">
            <div class="craft-art csm-art"><div class="craft-number">02</div><svg viewBox="0 0 160 220"><path d="M80 22 112 100 80 130 48 100z" fill="#d9d8ce" stroke="#f6f1e5" stroke-width="2"/><path d="M48 100 80 130 112 100 108 155 80 175 52 155z" fill="#aeb7b8"/><path d="M80 130v45m-28-20-23 22h28m51-22 23 22h-28" stroke="#d7a75e" stroke-width="4" fill="none"/><circle cx="80" cy="88" r="9" fill="#627987"/></svg></div>
            <div class="craft-info"><span>COMMAND & SERVICE MODULE</span><h3>Columbia</h3><p>The crew’s home for the journey. Collins remained in lunar orbit while the others explored the surface.</p><small>COMMAND MODULE + SERVICE MODULE</small></div>
          </article>
          <article class="craft-card">
            <div class="craft-art lm-art"><div class="craft-number">03</div><svg viewBox="0 0 160 220"><path d="M54 52 80 30 106 52 100 100 60 100z" fill="#c7c5b8" stroke="#f0eadb" stroke-width="2"/><path d="M60 100h40l20 38-40 26-40-26z" fill="#a7a99e"/><path d="M80 30V12m-26 40L30 35m76 17 24-17M40 138l-20 38h25m75-38 20 38h-25" stroke="#c5a16b" stroke-width="4" fill="none"/><path d="M65 66h30v20H65z" fill="#566f7b"/></svg></div>
            <div class="craft-info"><span>LUNAR MODULE</span><h3>Eagle</h3><p>The two-stage spacecraft that carried Armstrong and Aldrin down to the Sea of Tranquility and back to orbit.</p><small>DESCENT STAGE + ASCENT STAGE</small></div>
          </article>
        </div>
      </section>

      <section class="crew-section">
        <div class="crew-heading"><span class="section-index">06 / THE CREW</span><h2>Three explorers.<br><em>One extraordinary crew.</em></h2></div>
        <div class="crew-grid">
          <div class="crew-person"><span class="crew-index">COMMANDER</span><b>Neil<br>Armstrong</b><small>FIRST PERSON TO WALK ON THE MOON</small></div>
          <div class="crew-person"><span class="crew-index">COMMAND MODULE PILOT</span><b>Michael<br>Collins</b><small>REMAINED IN LUNAR ORBIT ABOARD COLUMBIA</small></div>
          <div class="crew-person"><span class="crew-index">LUNAR MODULE PILOT</span><b>Buzz<br>Aldrin</b><small>SECOND PERSON TO WALK ON THE MOON</small></div>
        </div>
      </section>

      <section class="ending">
        <div class="ending-stars"></div><span class="section-index">JULY 24, 1969 · 16:50:35 UTC</span>
        <h2>THE MISSION<br><em>WAS COMPLETE.</em></h2>
        <p>From a launch pad in Florida to another world and safely back again. Apollo 11 changed what humanity believed was possible.</p>
        <div class="ending-stamp">APOLLO 11 <span>✦</span> 1969</div>
      </section>
    </main>
    <footer><a class="brand footer-brand" href="#top"><span class="brand-mark">A<span>11</span></span><span class="brand-copy"><b>APOLLO 11</b><small>MISSION CONTROL</small></span></a><span>AN INTERACTIVE HISTORICAL EXPERIENCE</span><span>FOR ALL MANKIND · 1969</span></footer>
  `;
  renderEvents();
  bind();
  updateClock();
}

function renderEvents() {
  const list = document.querySelector('#eventList');
  list.innerHTML = events.map((e, i) => `
    <button class="event-row ${i === active ? 'selected' : ''}" data-index="${i}">
      <span class="event-number">${String(i + 1).padStart(2, '0')}</span>
      <span class="event-row-copy"><b>${e.title}</b><small>${e.day} · ${e.phase}</small></span>
      ${icon('chevron')}
    </button>
  `).join('');
  document.querySelectorAll('.event-row').forEach(btn => btn.addEventListener('click', () => {
    active = Number(btn.dataset.index);
    renderEvents();
  }));
  const e = events[active];
  document.querySelector('#eventDetail').innerHTML = `
    <div class="detail-top"><span>${e.phase}</span><span>EVENT ${String(active + 1).padStart(2, '0')} / 15</span></div>
    <div class="detail-date">${e.day} <i>·</i> ${e.time}</div>
    <h3>${e.title}</h3>
    <p class="detail-summary">${e.summary}</p>
    <p class="detail-body">${e.detail}</p>
    <div class="fact-grid">${e.facts.map(([k,v]) => `<div><small>${k}</small><b>${v}</b></div>`).join('')}</div>
    <div class="detail-controls"><button id="prevEvent" ${active === 0 ? 'disabled' : ''}>← PREVIOUS</button><button id="nextEvent" ${active === events.length - 1 ? 'disabled' : ''}>NEXT EVENT ${icon('arrow')}</button></div>
  `;
  document.querySelector('#prevEvent').addEventListener('click', () => { active = Math.max(0, active - 1); renderEvents(); });
  document.querySelector('#nextEvent').addEventListener('click', () => { active = Math.min(events.length - 1, active + 1); renderEvents(); });
}

function bind() {
  document.querySelector('#jumpLaunch').addEventListener('click', () => {
    active = 0; renderEvents(); document.querySelector('#timeline').scrollIntoView({ behavior: 'smooth' });
  });
  document.querySelector('#clockPlay').addEventListener('click', toggleClock);
  document.querySelector('#clockReset').addEventListener('click', () => {
    running = false; elapsedSeconds = 0; clearInterval(clockTimer);
    document.querySelector('#clockPlay').innerHTML = `${icon('play')} START CLOCK`;
    document.querySelector('#clockState').textContent = 'READY · T+00:00:00';
    updateClock();
  });
}

function toggleClock() {
  const btn = document.querySelector('#clockPlay');
  if (running) {
    clearInterval(clockTimer); running = false;
    btn.innerHTML = `${icon('play')} RESUME CLOCK`;
    document.querySelector('#clockState').textContent = 'PAUSED · MISSION CLOCK';
  } else {
    running = true;
    btn.innerHTML = `${icon('pause')} PAUSE CLOCK`;
    document.querySelector('#clockState').textContent = 'RUNNING · MISSION CLOCK';
    clockTimer = setInterval(() => { elapsedSeconds++; updateClock(); }, 1000);
  }
}

function updateClock() {
  const d = Math.floor(elapsedSeconds / 86400);
  const h = Math.floor((elapsedSeconds % 86400) / 3600);
  const m = Math.floor((elapsedSeconds % 3600) / 60);
  const s = elapsedSeconds % 60;
  document.querySelector('#clockReadout').innerHTML =
    `<span>${String(d).padStart(3, '0')}</span><small>DAYS</small><span>${String(h).padStart(2, '0')}</span><small>HRS</small><span>${String(m).padStart(2, '0')}</span><small>MIN</small><span>${String(s).padStart(2, '0')}</span><small>SEC</small>`;
  document.querySelector('#clockProgress').style.width = `${Math.min(100, elapsedSeconds / (8 * 86400 + 3 * 3600 + 18 * 60 + 35) * 100)}%`;
}

render();

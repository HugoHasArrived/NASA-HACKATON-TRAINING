# Apollo 11: The Journey

A browser-based, third-person/first-person educational Apollo 11 mission experience built with Three.js and Vite. The game follows Neil Armstrong's path from his early interest in aviation through NASA, Apollo-era preparation, launch, lunar operations and recovery.

> This is an independent educational simulation, not an official NASA product, an exact engineering model, or a certified astronaut-training system. Training scenarios simplify real procedures for learning and gameplay.

## Run locally

```bash
npm install
npm run dev
```

## Build for Vercel

- Framework preset: **Vite**
- Build command: `npm run build`
- Output directory: `dist`
- Install command: `npm install`

The included `vercel.json` supports Vite's static output. Import this repository into Vercel after pushing it to GitHub.

## Controls

- `W A S D`: move
- Mouse: look around (click the scene to capture pointer)
- `E`: interact
- `Shift`: move faster
- On the launch flight deck: `W/S` throttle, arrow keys pitch/yaw, throttle slider and staging/TLI controls
- Touch controls are available on touch-screen devices

## Training modules

The six interactive stations are based on documented Apollo-era preparation themes:

1. Flight procedures and checklist discipline
2. Pressure suit / life-support pre-EVA verification
3. Rendezvous and docking relative-motion control
4. Lunar geology and contextual sample selection
5. Lunar Module powered-descent control
6. Abnormal-procedure response and crew communication

Each station includes an evaluated hands-on task, feedback, and a pass state. All six must be passed before the training-floor mission gate opens.

## Historical basis and further reading

- NASA, [Building on a Mission: Astronaut Training Facilities](https://www.nasa.gov/history/building-on-a-mission-astronaut-training-facilities/) — Gemini and Apollo Command Module, Lunar Module and docking simulators; Water Immersion Facility.
- NASA, [50 Years Ago: Apollo 11 Preparations, February 1969](https://www.nasa.gov/history/50-years-ago-apollo-11-preparations-february-1969/) — Apollo 11 geology field training and lunar surface science preparation.
- NASA, [Building on a Mission: Neutral Buoyancy Facilities for Spacewalk Training](https://www.nasa.gov/history/building-on-a-mission-neutral-buoyancy-facilities-for-spacewalk-training/) — Apollo-era water-immersion work and Armstrong/Aldrin lunar-gravity simulation.
- NASA, [Apollo Expeditions to the Moon: Training Crews and Controllers](https://www.nasa.gov/wp-content/uploads/static/history/SP-350/ch-7-8.html) — zero-gravity aircraft, water tank training and Lunar Landing Training Vehicle.

The in-game exercises are newly written simplifications inspired by these historical practices. They do not reproduce NASA's complete crew syllabus, flight software, checklists, or operational limits.

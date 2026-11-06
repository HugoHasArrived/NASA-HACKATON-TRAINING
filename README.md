# Mission Control — Space Mission Design Game

An independent educational game prototype inspired by the **2026 NASA Space Apps Challenge: Space Mission Design Game**. The primary experience is a mission-design workbench: define a science objective, configure a spacecraft, select instruments, choose a launch vehicle and orbit, manage limited resources, and run a mission simulation. Apollo 11 remains available as a separate historical 3D case study.

## Challenge alignment

- **Mission objectives:** lunar water-ice mapping, Mars geology, Earth climate monitoring, and near-Earth asteroid characterisation.
- **Spacecraft design:** selectable spacecraft bus, redundant avionics, antenna, solar arrays and science payload.
- **Payload trade-offs:** each instrument changes mass, power demand, data volume, programme cost and science score.
- **Launch and orbit:** compare launcher payload capacities and select a trajectory/orbit matched to the mission objective.
- **Resource dashboard:** live mass, power, data/downlink and budget checks, plus mission lifetime, compatibility and science potential.
- **Game modes:** Beginner/Youth, Intermediate and Advanced scoring; Challenge and Sandbox modes.
- **Simulation and evaluation:** random operational events, constraint warnings, mission score, grade and engineering debrief.
- **Save/load:** save a design in browser local storage and load it again on the same browser/device.
- **Team collaboration concept:** four role cards for Mission Director, Spacecraft Engineer, Science Lead and Flight Dynamics. This is a role-based team-play scaffold, not live network multiplayer.
- **Historical case study:** optional Apollo 11 3D experience with training activities, flight sequence, maps and mission timeline.

## Run locally

```bash
npm install
npm run dev
```

## Build and deploy

- Framework preset: **Vite**
- Build command: `npm run build`
- Output directory: `dist`
- Install command: `npm install`

Push the project to GitHub and import the repository into Vercel. The included `vercel.json` supports Vite static output.

## Controls for the optional Apollo 11 3D case study

- `W A S D`: move
- Mouse: look around (click the scene to capture pointer)
- `E`: interact
- `Shift`: move faster
- Flight deck: `W/S` throttle, arrow keys pitch/yaw, throttle slider and staging/TLI controls
- Touch controls are available on touch-screen devices

## Important modelling note

This is a learning game, not a flight dynamics tool. Resource values, costs, payload capacities, science points, orbit matching and scoring are **illustrative game-balance assumptions** rather than real mission design data, engineering requirements, procurement estimates or validated vehicle performance. The simulation does not calculate orbital mechanics, propulsion, thermal behaviour, radiation, link budgets, power storage sizing or reliability statistically. Use it to explore connected trade-offs, not to make real spacecraft decisions.

## Team mode status

The prototype presents four complementary team roles and supports a shared discussion workflow on one device. Real-time multiplayer, user accounts, remote synchronisation, team invitations and a public leaderboard are not implemented.

## NASA historical resources

- [Building on a Mission: Astronaut Training Facilities](https://www.nasa.gov/history/building-on-a-mission-astronaut-training-facilities/)
- [50 Years Ago: Apollo 11 Preparations, February 1969](https://www.nasa.gov/history/50-years-ago-apollo-11-preparations-february-1969/)
- [Building on a Mission: Neutral Buoyancy Facilities for Spacewalk Training](https://www.nasa.gov/history/building-on-a-mission-neutral-buoyancy-facilities-for-spacewalk-training/)
- [Apollo Expeditions to the Moon: Training Crews and Controllers](https://www.nasa.gov/wp-content/uploads/static/history/SP-350/ch-7-8.html)

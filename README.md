# Apollo 11 — The Journey

A Vite + Three.js educational Apollo 11 story game.

## Run locally

```bash
npm install
npm run dev
```

## Production build

```bash
npm run build
```

Vercel settings:
- Framework: Vite
- Build command: `npm run build`
- Output directory: `dist`
- Install command: `npm install`

## Important GitHub upload note

Keep `index.html`, `main.js`, `style.css`, `package.json`, and `vercel.json` together in the repository root. Do not upload only `index.html`; the JavaScript entry file and stylesheet are required.

This is an independent educational simulation, not an official NASA product or NASA-certified training.

## Flight controls

In the Saturn V launch chapter, click **IGNITION / LIFTOFF**, adjust the throttle slider (or use **W/S**), and steer with **↑/↓** for pitch and **←/→** for yaw. Confirm the stage-separation milestones, then select **TRANS-LUNAR INJECTION** when Earth parking orbit is reached. The flight model is a simplified educational game mechanic, not a NASA flight simulator or physically validated trajectory model.

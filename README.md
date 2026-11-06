# Apollo 11 — The Journey

An interactive, chapter-based Apollo 11 educational game built with Vite and Three.js.

## Chapters and navigation

The opening screen is the homepage. Select **Begin Journey** to enter the 3D story. Use **CHAPTERS** in the upper-right HUD to open the chapter navigator and jump directly to any scene; use **HOME** to return to the homepage.

1. **Life on Earth** — an apartment-style scene about Neil Armstrong's childhood in Wapakoneta, early flying, education, Navy service, and test-pilot career.
2. **NASA / Manned Spacecraft Center** — a simulated mission-roster registration and the real story of Armstrong's 1962 astronaut selection and Gemini 8 mission. The Houston center is shown because astronaut operations and Apollo training were based there; NASA Headquarters itself is in Washington, D.C.
3. **Astronaut Training** — interactive stations covering checklists, lunar geology, teamwork, and spacecraft orientation. These are educational recreations, not certified NASA training.
4. **Saturn V Launch** — launch pad, throttle, liftoff, staged ascent, Earth parking orbit, and trans-lunar injection.
5. **The Moon** — lunar orbit and Eagle landing story, first footprints, surface science and samples, ascent, and rendezvous with Columbia.
6. **Return to Earth** — trans-Earth return, Pacific splashdown on July 24, USS Hornet recovery, and quarantine.

## Run locally

```bash
npm install
npm run dev
```

## Production build

```bash
npm run build
```

## Vercel

- Framework preset: Vite
- Build command: `npm run build`
- Output directory: `dist`
- Install command: `npm install`

Keep `index.html`, `main.js`, `style.css`, `package.json`, and `vercel.json` together in the repository root.

## Controls

- Walk: `W A S D`; look: mouse; interact: `E`; move faster: `Shift`.
- Flight deck: throttle slider or `W/S`; pitch: `↑/↓`; yaw: `←/→`.
- Press **IGNITION / LIFTOFF**, use the staging control at each staging milestone, and select **TRANS-LUNAR INJECTION** after reaching the simplified parking-orbit threshold.
- On touch devices, use the on-screen movement pad, drag-to-look area, and USE button.

The flight dynamics are simplified game mechanics and are not a physically validated trajectory or flight-certified simulator. The project is independent and is not an official NASA product.

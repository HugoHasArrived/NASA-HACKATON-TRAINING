# Apollo 11 — The Journey

An independent, browser-based Apollo 11 story adventure built with Vite and Three.js. It follows Neil Armstrong's documented path from his early interest in aviation, through NASA selection and Gemini 8, into Apollo-era training and the July 1969 lunar mission. The launch chapter includes a simplified, player-controlled Saturn V ascent.

> This is an educational historical simulation, not an official NASA product, an exact reconstruction of NASA astronaut training, or a flight-certified simulator. The apartment-style opening is a fictionalized story setting rather than a reconstruction of Armstrong’s actual home. The astronaut-training stations are historically inspired learning activities. Rocket physics and mission time are simplified for interactive gameplay.

## Run locally

```bash
npm install
npm run dev
```

Open the local URL printed by Vite.

## Build for production

```bash
npm run build
npm run preview
```

## Deploy with GitHub + Vercel

1. Extract this ZIP file.
2. Create a new GitHub repository.
3. Upload the contents of this folder to the repository root. `index.html`, `main.js`, `style.css`, `package.json`, and `vercel.json` must remain together.
4. In Vercel, choose **Add New → Project**, import the GitHub repository, and deploy.
5. Vercel settings: Framework **Vite**, Build Command `npm run build`, Output Directory `dist`, Install Command `npm install`.

The included `vercel.json` routes browser requests to the Vite app entry point.

## Controls

### Walking/story chapters
- `W A S D`: walk
- Mouse: look around (click the scene to capture the mouse)
- `E`: interact with a highlighted station
- `Shift`: move faster
- Mobile: on-screen directional pad, drag-to-look area, and Use button

### Saturn V flight deck
- Click **IGNITION / LIFTOFF** to begin the launch sequence.
- Use the throttle slider or `W` / `S` to change throttle.
- Use `↑` / `↓` to adjust pitch and `←` / `→` to adjust yaw. These inputs alter the simplified ascent path and rocket attitude.
- At the appropriate altitude, use **STAGE SEPARATION** to jettison the S-IC and then S-II stages in sequence.
- Reach the simulated Earth parking orbit and complete the stage sequence before selecting **TRANS-LUNAR INJECTION**.

The game compresses mission events and uses a simplified control model. It is designed to teach the sequence and context of Apollo 11, not to reproduce actual Saturn V guidance, real-time mission elapsed time, or NASA operational procedures.

## Historical reference points represented

- Launch: July 16, 1969, 13:32 UTC, Kennedy Space Center Launch Complex 39A.
- Lunar orbit insertion: July 19, 1969.
- Eagle lunar landing: July 20, 1969, 20:17 UTC, Sea of Tranquility.
- Armstrong's first step: July 21, 1969, 02:56 UTC (20:56 EDT on July 20).
- Pacific splashdown: July 24, 1969. Total mission duration: 8 days, 3 hours, 18 minutes, 35 seconds.

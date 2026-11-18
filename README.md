# my-first-project
Learning GitHub basics

## 💧 Sip — hydration tracker (`hydration/`)

A small phone web app (PWA) for tracking how much water you drink and reminding you to drink more.

- Tap +250 / +350 / +500 ml (or 8 / 12 / 16 oz), or enter your own amount
- A progress ring toward your daily goal, today's log with undo, and a 7-day history
- Reminders every 30 min to 2 hrs between the start and end times you choose (a notification plus an in-app alert while the app is open)
- **📅 Add reminders to my phone's calendar** downloads an `.ics` file of repeating daily alarms, so you get reminded even when the app is closed
- Your data stays on your phone (localStorage), and the app works offline

**Install on your phone:** host the folder (e.g. GitHub Pages), open it on your phone, then use *Share → Add to Home Screen* (iPhone) or *⋮ → Add to Home screen* (Android).

### Android app (`sip-android/`)

The same app packaged as a native Android app with [Capacitor](https://capacitorjs.com). Reminders use Android's own scheduled notifications, so they arrive even when Sip is closed. They're scheduled a week ahead, wait one interval after you log a drink, stop for the day once you reach your goal, and include a "+250 ml" button.

Build it (needs Node, JDK 21 and the Android SDK, with `ANDROID_HOME` set):

```bash
cd sip-android
npm install
npm run build:apk   # -> android/app/build/outputs/apk/debug/app-debug.apk
```

#!/usr/bin/env python3
"""
Generator script to build modern, glassmorphic landing pages for all apps
in Rj707.github.io following Approach B (Pre-Launch Early Access & Coming Soon).
"""

import os
import shutil

APPS = {
    "zen-focus": {
        "name": "Zen Focus",
        "title": "Zen Focus — Calm Pomodoro & Tactile Ambient Timer",
        "slug": "zen-focus",
        "tagline": "Focus • Meditate • Flow",
        "badge": "✨ In Active Development • Coming Soon to iOS & Android",
        "hero_desc": "An intentional, distraction-free productivity chronometer crafted for ADHD focus, study marathons, deep programming sessions, and mindful deep work. Features an analog rotary tactile dial paired with a 6-channel offline ambient soundscape generator.",
        "icon": "assets/icon.png",
        "primary_color": "#F59E0B",
        "accent_color": "#10B981",
        "glow_color": "rgba(245, 158, 11, 0.22)",
        "email": "rajasaad707+zenfocus@gmail.com",
        "features": [
            {
                "icon": "⏱️",
                "title": "Tactile Rotary Dial",
                "text": "Smooth, fluid, physics-driven analog rotary chronometer. Dial in focus intervals instantly with satisfying micro-haptics."
            },
            {
                "icon": "🌧️",
                "title": "6-Channel Offline Soundscapes",
                "text": "Mix rain, brown noise, cozy fireplace, forest wind, cafe chatter, and ocean waves. 100% bundled locally on your device."
            },
            {
                "icon": "🖤",
                "title": "OLED Pure Black Aesthetic",
                "text": "Genuine #000000 high-contrast interface engineered to eliminate eye fatigue and save battery life during marathon sessions."
            },
            {
                "icon": "⚡",
                "title": "Zero-Friction Flow",
                "text": "Zero accounts, no email logins, no intrusive popups. Open the app and plunge into deep work in under 3 seconds."
            },
            {
                "icon": "📊",
                "title": "Private Focus Analytics",
                "text": "Track streaks, total focus minutes, and daily productivity heatmaps. All analytics are stored strictly on-device."
            },
            {
                "icon": "💎",
                "title": "Anti-Subscription Promise",
                "text": "No monthly or yearly recurring traps. Honest, transparent, one-time lifetime access with zero telemetry."
            }
        ],
        "screenshots": [
            ("01_hero_dial.png", "Tactile Rotary Dial"),
            ("02_ambient_mixer.png", "6-Channel Soundscapes"),
            ("03_stats_streak.png", "Focus Analytics & Streaks"),
            ("04_lifetime_paywall.png", "Lifetime Unlock")
        ],
        "faqs": [
            ("Does Zen Focus require an internet connection?", "No. Zen Focus is 100% offline-first. All soundscapes, timer engines, and focus analytics function perfectly in airplane mode."),
            ("Are there any monthly subscription fees?", "Never. Zen Focus is built on a single, affordable one-time lifetime purchase. You own all current and future updates forever."),
            ("How does Zen Focus protect my privacy?", "Zen Focus collects zero personal data, creates no online profiles, and contains zero trackers. Your deep work history never leaves your device.")
        ],
        "legal_type": "utility"
    },
    "fluid-glow": {
        "name": "Fluid Glow",
        "title": "Fluid Glow — ASMR Sensory Relax & Dynamic Shaders",
        "slug": "fluid-glow",
        "tagline": "Touch • Relax • Mesmerize",
        "badge": "✨ In Active Development • Coming Soon to iOS & Android",
        "hero_desc": "Mesmerizing real-time liquid physics simulation with glowing neon particle shaders, calming ambient audio, and responsive multi-touch fluid dynamics. A soothing digital playground engineered for sensory calm, focus, and stress relief.",
        "icon": "assets/icon.png",
        "primary_color": "#00E5FF",
        "accent_color": "#FF375F",
        "glow_color": "rgba(0, 229, 255, 0.22)",
        "email": "rajasaad707+fluidglow@gmail.com",
        "features": [
            {
                "icon": "🌊",
                "title": "Navier-Stokes Fluid Engine",
                "text": "High-performance GPU-accelerated fluid dynamics supporting multi-finger swirling, vortex generation, and viscous flow."
            },
            {
                "icon": "✨",
                "title": "12+ Dynamic Shaders",
                "text": "Switch between Electric Neon, Deep Space Nebula, Aurora Borealis, Liquid Gold, and Fire Glow shader presets."
            },
            {
                "icon": "🎧",
                "title": "ASMR Ambient Audio",
                "text": "Subtle, soothing generative audio chords and delicate micro-haptics synced dynamically to every fluid ripple."
            },
            {
                "icon": "📱",
                "title": "Interactive Live Wallpaper",
                "text": "Set your personalized fluid creations as your home screen or lock screen wallpaper for instant calming moments."
            },
            {
                "icon": "🎛️",
                "title": "Deep Physics Customizer",
                "text": "Fine-tune viscosity, bloom intensity, particle lifespan, vorticity, pressure iterations, and color palettes."
            },
            {
                "icon": "🔒",
                "title": "100% Offline & Private",
                "text": "No logins, no ads during flow, and zero personal tracking. Complete relaxation wherever you are."
            }
        ],
        "screenshots": [
            ("screenshot_1_hero.png", "Real-Time Fluid Simulation"),
            ("screenshot_2_wallpaper.png", "Interactive Wallpapers"),
            ("screenshot_3_shaders.png", "12+ Trippy Shaders"),
            ("screenshot_4_vip.png", "Lifetime VIP Pass"),
            ("screenshot_5_guide.png", "Custom Physics Controls")
        ],
        "faqs": [
            ("Can I use Fluid Glow as my live wallpaper?", "Yes, on supported iOS and Android devices, you can set the interactive fluid physics directly as your live background."),
            ("Does the simulation drain battery heavily?", "No. The physics engine is compiled to native Metal / Vulkan shaders, dynamically pausing computation when the screen is idle."),
            ("Is Fluid Glow safe for children?", "Yes, Fluid Glow is 100% COPPA certified with no social features, no external chat, and child-safe content.")
        ],
        "legal_type": "creative"
    },
    "tinysteps": {
        "name": "TinySteps",
        "title": "TinySteps — Baby Milestones & Daily Tracker",
        "slug": "tinysteps",
        "tagline": "Track • Cherish • Remember",
        "badge": "✨ In Active Development • Coming Soon to iOS & Android",
        "hero_desc": "Private, secure baby growth, feeding, sleep, diaper, and developmental milestone tracker designed specifically for sleep-deprived parents. Effortless one-handed logging, WHO growth percentiles, and zero third-party data tracking.",
        "icon": "assets/icon.png",
        "primary_color": "#FB7185",
        "accent_color": "#FBBF24",
        "glow_color": "rgba(251, 113, 133, 0.22)",
        "email": "rajasaad707+tinysteps@gmail.com",
        "features": [
            {
                "icon": "🍼",
                "title": "1-Tap Quick Logging",
                "text": "Log nursing, bottle feeding, pumping, sleep intervals, and diaper changes with one-handed ease during late-night feeds."
            },
            {
                "icon": "📈",
                "title": "Official WHO Growth Charts",
                "text": "Track weight, height, and head circumference against World Health Organization growth curves and percentile calculations."
            },
            {
                "icon": "🌟",
                "title": "Developmental Milestones",
                "text": "Celebrate first smiles, rolling over, babbling, and first steps with pediatrician-aligned milestone checklists."
            },
            {
                "icon": "📸",
                "title": "Private Photo Journal",
                "text": "Attach milestone photos and memories to a secure, private baby timeline that stays on your device."
            },
            {
                "icon": "⏰",
                "title": "Smart Reminders & Schedules",
                "text": "Predict nap times and diaper intervals with gentle, customizable notifications that fit your baby's rhythm."
            },
            {
                "icon": "🛡️",
                "title": "100% Child Data Privacy",
                "text": "Zero third-party data sharing. Your baby's intimate growth data and photos are never sold or used for ad targeting."
            }
        ],
        "screenshots": [
            ("01_hero.png", "Daily Dashboard"),
            ("02_tracking.png", "1-Tap Logging"),
            ("03_milestones.png", "Developmental Milestones"),
            ("04_charts.png", "WHO Growth Charts"),
            ("05_journal.png", "Precious Moments Journal"),
            ("06_vip.png", "Family Lifetime Access")
        ],
        "faqs": [
            ("Is my baby's health data kept private?", "Yes, 100%. TinySteps is built on a strict privacy-first foundation. All logs, health notes, and photos stay on your device and are never monetized."),
            ("Can both parents sync data between devices?", "Yes, private family synchronization via Apple iCloud / Google Cloud allows both parents to log and see updates in real-time."),
            ("Does TinySteps work offline?", "Yes, all tracking features work seamlessly offline. Logs automatically synchronize whenever your network becomes available.")
        ],
        "legal_type": "family"
    },
    "reader-lab": {
        "name": "Reader Lab",
        "title": "Reader Lab — Speed Reading & Bionic Comprehension",
        "slug": "reader-lab",
        "tagline": "Read Faster • Retain More • Master Knowledge",
        "badge": "✨ In Active Development • Coming Soon to iOS & Android",
        "hero_desc": "Modern cognitive speed reading assistant combining Bionic fixation points, RSVP rapid serial streaming, and peripheral vision pacing tools. Double your reading speed while maximizing retention and reducing eye fatigue.",
        "icon": "assets/icon.png",
        "primary_color": "#6366F1",
        "accent_color": "#8B5CF6",
        "glow_color": "rgba(99, 102, 241, 0.22)",
        "email": "rajasaad707+readerlab@gmail.com",
        "features": [
            {
                "icon": "👁️",
                "title": "Bionic Reading Engine",
                "text": "Smart typographic fixation points emphasize initial letters, letting your brain automatically complete words with minimal eye jumps."
            },
            {
                "icon": "⚡",
                "title": "RSVP Rapid Streamer",
                "text": "Stream words sequentially at speeds from 250 to 1,000 WPM, eliminating subvocalization and visual tracking fatigue."
            },
            {
                "icon": "📚",
                "title": "EPUB, PDF & Web Importer",
                "text": "Import your favorite books, articles, and research papers with clean, distraction-free reader mode styling."
            },
            {
                "icon": "🎯",
                "title": "Eye Training Drills",
                "text": "Interactive peripheral expansion drills and saccade pacing exercises scientifically engineered to broaden visual span."
            },
            {
                "icon": "📖",
                "title": "Dyslexia-Friendly Fonts",
                "text": "Includes OpenDyslexic, Atkinson Hyperlegible, and custom line-height and contrast controls for accessible reading."
            },
            {
                "icon": "🔒",
                "title": "Private Document Storage",
                "text": "Imported books and reading materials are stored locally. Your library is 100% private and never indexed."
            }
        ],
        "screenshots": [
            ("01_hero.png", "Bionic Reader View"),
            ("02_rsvp.png", "RSVP Speed Streamer"),
            ("03_bionic.png", "Reading Speed Drills"),
            ("04_library.png", "EPUB & PDF Library"),
            ("05_stats.png", "Comprehension Analytics")
        ],
        "faqs": [
            ("What document formats can I import?", "Reader Lab supports standard EPUB, PDF, TXT, Markdown, and direct web URL imports."),
            ("How does Bionic Reading increase speed?", "By highlighting key initial syllables, your eye fixates on fewer points while your brain seamlessly predicts the complete word."),
            ("Does Reader Lab upload my personal books?", "No. All imported documents are processed and parsed strictly on-device. No books are ever uploaded to external servers.")
        ],
        "legal_type": "education"
    },
    "slide-routes": {
        "name": "Slide Routes",
        "title": "Slide Routes — Block Escape Puzzle",
        "slug": "slide-routes",
        "tagline": "Slide • Unblock • Escape",
        "badge": "✨ In Active Development • Coming Soon to iOS & Android",
        "hero_desc": "Elegant, minimalist sliding block puzzle with 60+ handcrafted logic levels, dual-target mazes, tactile wooden haptics, and intelligent hint assistance. Pure offline brain-teasing relaxation with zero time pressure.",
        "icon": "assets/icon.png",
        "primary_color": "#10B981",
        "accent_color": "#14B8A6",
        "glow_color": "rgba(16, 185, 129, 0.22)",
        "email": "rajasaad707+slideroutes@gmail.com",
        "features": [
            {
                "icon": "🧩",
                "title": "60+ Handcrafted Mazes",
                "text": "Carefully balanced stages progressing smoothly from accessible warmups to mind-bending grandmaster puzzles."
            },
            {
                "icon": "🎯",
                "title": "Dual-Target Escape Goals",
                "text": "Route multiple colored blocks into synchronized exit portals requiring clever foresight and spatial maneuvers."
            },
            {
                "icon": "💡",
                "title": "Step-by-Step Hint Engine",
                "text": "Never get frustratingly stuck. Use smart hints to illuminate the next optimal sequence of slide maneuvers."
            },
            {
                "icon": "🪵",
                "title": "Tactile Wooden Haptics",
                "text": "Crisp, organic haptic clicks and pleasant acoustic wood chimes accompany every sliding maneuver."
            },
            {
                "icon": "🧘",
                "title": "Zen Relaxing Atmosphere",
                "text": "No countdown timers, no star deductions, and no arbitrary penalties. Ponder each move in serene peace."
            },
            {
                "icon": "✈️",
                "title": "100% Offline Gameplay",
                "text": "Zero Wi-Fi or cellular connection required. Perfect for flights, daily commutes, and quiet evenings."
            }
        ],
        "screenshots": [
            ("01_01_escape_the_grid.png", "Escape the Grid"),
            ("02_02_60_levels_catalog.png", "60+ Levels Catalog"),
            ("03_03_dual_target_mazes.png", "Dual Target Mazes"),
            ("04_04_smart_hint_engine.png", "Smart Hint Engine"),
            ("05_05_offline_zen_logic.png", "Offline Zen Logic")
        ],
        "faqs": [
            ("Are there time limits or move counters?", "No. Slide Routes is built as a relaxing logic puzzle with no stressful timers. Solve at your own natural pace."),
            ("Can I play without an internet connection?", "Yes. All 60+ levels and hint systems work 100% offline with zero data consumption."),
            ("How do I restore purchases?", "A single tap on 'Restore Purchases' in Settings automatically restores your Lifetime Pass on any iOS or Android device.")
        ],
        "legal_type": "game"
    },
    "pocket-sort": {
        "name": "Pocket Sort",
        "title": "Pocket Sort — Color Puzzle Quest",
        "slug": "pocket-sort",
        "tagline": "Sort • Match • Unwind",
        "badge": "✨ In Active Development • Coming Soon to iOS & Android",
        "hero_desc": "Clean, deeply satisfying color sorting puzzle game. Organize colorful liquids into test tubes, train your cognitive spatial reasoning, and relax with smooth fluid pouring animations and peaceful ambient sounds.",
        "icon": "assets/icon.png",
        "primary_color": "#4E95FF",
        "accent_color": "#9D4EDD",
        "glow_color": "rgba(78, 149, 255, 0.22)",
        "email": "rajasaad707+pocketsort@gmail.com",
        "features": [
            {
                "icon": "🧪",
                "title": "100+ Addictive Levels",
                "text": "Progress from simple 3-flask challenges to intricate multi-tube puzzles that test your cognitive planning."
            },
            {
                "icon": "💧",
                "title": "Fluid Pouring Physics",
                "text": "Smooth liquid animations and satisfying splashing acoustics make every color pour a sensory pleasure."
            },
            {
                "icon": "↩️",
                "title": "Unlimited Undo Power",
                "text": "Experiment freely without fear. Step back mistakes instantly and explore alternative sorting paths."
            },
            {
                "icon": "➕",
                "title": "Extra Tube Power-Up",
                "text": "When facing a tight bottleneck, summon a spare tube to unlock room for strategic maneuvering."
            },
            {
                "icon": "🎨",
                "title": "Vibrant Flask Themes",
                "text": "Unlock custom glassware shapes, sparkling liquid colors, and relaxing backdrop atmospheres."
            },
            {
                "icon": "🧸",
                "title": "Safe Family Friendly",
                "text": "Zero vulgarity, family-certified ad filtering, and offline support suitable for puzzle fans of all ages."
            }
        ],
        "screenshots": [],
        "faqs": [
            ("Is Pocket Sort free to play?", "Yes, you can play through hundreds of levels for free. An optional one-time pass removes ads completely."),
            ("What happens if I get stuck?", "You can use the 'Undo' button to rewind moves, or add an extra empty tube to create more sorting space."),
            ("Does the game collect any personal data?", "No personal data is collected or stored. All level progress is saved strictly on your local device.")
        ],
        "legal_type": "game"
    },
    "numbers123": {
        "name": "Numbers 123",
        "title": "Numbers 123 — Kids Tracing & Counting",
        "slug": "numbers123",
        "tagline": "Trace • Count • Learn",
        "badge": "✨ In Active Development • Coming Soon to iOS & Android",
        "hero_desc": "Vibrant, interactive early math and number tracing app for toddlers and preschoolers. Learn number formations, cheerful audio phonics, animal counting games, and foundational logic in a safe, child-first environment.",
        "icon": "assets/icon.png",
        "primary_color": "#FACC15",
        "accent_color": "#FB923C",
        "glow_color": "rgba(250, 204, 21, 0.22)",
        "email": "rajasaad707+numbers123@gmail.com",
        "features": [
            {
                "icon": "✏️",
                "title": "Guided Number Tracing",
                "text": "Animated stroke directions and sparkle rewards guide little fingers to learn proper number writing effortlessly."
            },
            {
                "icon": "🔊",
                "title": "Audio Phonics & Cheers",
                "text": "Enthusiastic child-friendly voiceovers pronounce numbers, counting sequences, and joyful congratulatory cheers."
            },
            {
                "icon": "🦁",
                "title": "Interactive Counting Games",
                "text": "Count colorful animals, fruits, stars, and shapes with touch feedback that builds foundational arithmetic intuition."
            },
            {
                "icon": "🔒",
                "title": "Parental Gate Protection",
                "text": "Adult-only math gates protect settings and external links, ensuring toddlers cannot accidentally navigate away."
            },
            {
                "icon": "🛡️",
                "title": "COPPA Certified Child Safe",
                "text": "Zero third-party tracking, zero behavioral profiling, and strict adherence to Apple & Google Kids Family policies."
            },
            {
                "icon": "✈️",
                "title": "100% Offline Roadtrip Ready",
                "text": "Enjoy on car rides, plane trips, and restaurants without needing internet, Wi-Fi, or cellular connectivity."
            }
        ],
        "screenshots": [],
        "faqs": [
            ("What age group is Numbers 123 designed for?", "Numbers 123 is specifically tailored for toddlers, preschoolers, and kindergarteners ages 2 to 6."),
            ("Are there any ads or external links accessible to kids?", "No. The app strictly enforces child safety with adult-only parental gates and complies fully with COPPA and Google Play Families policy."),
            ("Can my child play without an internet connection?", "Yes! Numbers 123 is 100% offline. All audio narrations, animations, and games are bundled directly inside the app.")
        ],
        "legal_type": "kids"
    },
    "ar-drawing": {
        "name": "AR Drawing",
        "title": "AR Drawing — Paint & Sketch Art",
        "slug": "ar-drawing",
        "tagline": "Trace • Sketch • Master Art",
        "badge": "✨ In Active Development • Coming Soon to iOS & Android",
        "hero_desc": "Transform your smartphone into an augmented reality sketching projector. Place your phone on a glass or stand, trace any template onto physical paper with AR camera overlays, and learn to sketch like a master artist in minutes.",
        "icon": "assets/icon.png",
        "primary_color": "#A855F7",
        "accent_color": "#EC4899",
        "glow_color": "rgba(168, 85, 247, 0.22)",
        "email": "rajasaad707+ardrawing@gmail.com",
        "features": [
            {
                "icon": "📷",
                "title": "Optical AR Camera Projection",
                "text": "Project digital sketches directly through your camera onto real paper, canvas, or walls for flawless tracing."
            },
            {
                "icon": "🎨",
                "title": "100+ Curated Sketch Stencils",
                "text": "Rich library of templates across Anime, Manga, Animals, Chibi, Nature, Tattoo Art, and Classical Architecture."
            },
            {
                "icon": "🖼️",
                "title": "Convert Photos to Outlines",
                "text": "Advanced edge-detection transforms any photo from your gallery into a crisp, high-contrast sketch template."
            },
            {
                "icon": "🔒",
                "title": "Touch-Lock Drawing Mode",
                "text": "Lock screen touch controls while drawing so accidental palm brushes never nudge or misalign your projected stencil."
            },
            {
                "icon": "💡",
                "title": "Flashlight & Opacity Slider",
                "text": "Draw in any lighting condition with built-in torch controls and variable stencil opacity calibration."
            },
            {
                "icon": "🛡️",
                "title": "100% Private On-Device Vision",
                "text": "Your camera stream and personal photos are processed locally in RAM and are never uploaded or recorded."
            }
        ],
        "screenshots": [
            ("01_01_trace_on_paper.png", "Trace on Real Paper"),
            ("02_02_easy_stand_setup.png", "Easy Stand Setup"),
            ("03_03_sketch_templates.png", "100+ Sketch Templates"),
            ("04_04_touch_lock_mode.png", "Touch-Lock Drawing Mode"),
            ("05_05_convert_any_photo.png", "Convert Photos to Sketches")
        ],
        "faqs": [
            ("How do I set up my phone for drawing?", "Simply place your phone on a cup, water bottle, or desktop tripod above a blank sheet of paper, align the camera, and trace through the screen."),
            ("Does AR Drawing work with my own personal photos?", "Yes! You can pick any photo from your camera roll, and our AI edge-filter will instantly convert it into a trace-friendly outline."),
            ("Is my camera feed private?", "Yes, absolutely. The camera feed is strictly utilized in real-time to overlay the stencil and is never transmitted to any external server.")
        ],
        "legal_type": "creative"
    }
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{hero_desc}">
    <link rel="icon" type="image/png" href="{icon}">
    
    <style>
        :root {{
            --bg: #07090e;
            --surface: #0f131d;
            --surface-elevated: #151b28;
            --border: rgba(255, 255, 255, 0.08);
            --border-hover: {primary_color};
            --primary: {primary_color};
            --primary-glow: {glow_color};
            --accent: {accent_color};
            --text: #f8fafc;
            --text-sec: #94a3b8;
            --text-muted: #64748b;
            --font: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: var(--font);
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }}

        /* Ambient Glow Background */
        .ambient-bg {{
            position: fixed;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 0;
            background: 
                radial-gradient(circle at 50% 8%, {glow_color} 0%, transparent 55%),
                radial-gradient(circle at 82% 35%, rgba(255, 55, 95, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 18% 65%, rgba(168, 85, 247, 0.07) 0%, transparent 50%);
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 24px;
            position: relative;
            z-index: 1;
        }}

        /* Sticky Glass Navbar */
        nav {{
            position: sticky;
            top: 0;
            z-index: 100;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            background: rgba(7, 9, 14, 0.85);
            border-bottom: 1px solid var(--border);
        }}

        .nav-content {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 70px;
        }}

        .logo {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: var(--text);
            font-weight: 700;
            font-size: 1.22rem;
            letter-spacing: -0.02em;
        }}

        .logo img {{
            width: 38px;
            height: 38px;
            border-radius: 10px;
            box-shadow: 0 4px 14px var(--primary-glow);
            object-fit: cover;
        }}

        .nav-links {{
            display: flex;
            align-items: center;
            gap: 26px;
            list-style: none;
        }}

        .nav-links a {{
            color: var(--text-sec);
            text-decoration: none;
            font-size: 0.94rem;
            font-weight: 500;
            transition: color 0.2s;
        }}

        .nav-links a:hover {{
            color: var(--text);
        }}

        .nav-cta {{
            background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
            color: #ffffff !important;
            padding: 9px 20px;
            border-radius: 999px;
            font-weight: 600 !important;
            box-shadow: 0 4px 14px var(--primary-glow);
            transition: transform 0.2s, box-shadow 0.2s !important;
            border: 1px solid rgba(255, 255, 255, 0.15);
            cursor: pointer;
        }}

        .nav-cta:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px var(--primary-glow) !important;
        }}

        /* Hero Section */
        .hero {{
            text-align: center;
            padding: 70px 0 60px;
        }}

        .badge-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 7px 18px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: var(--primary);
            font-size: 0.88rem;
            font-weight: 600;
            margin-bottom: 26px;
        }}

        .hero-icon {{
            width: 110px;
            height: 110px;
            border-radius: 26px;
            margin: 0 auto 24px;
            box-shadow: 0 16px 40px var(--primary-glow), 0 0 0 1px rgba(255, 255, 255, 0.1);
            display: block;
            object-fit: cover;
        }}

        .hero-tagline {{
            display: block;
            font-size: 0.95rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--primary);
            margin-bottom: 12px;
        }}

        .hero h1 {{
            font-size: 3rem;
            line-height: 1.15;
            font-weight: 800;
            letter-spacing: -0.03em;
            margin-bottom: 18px;
            background: linear-gradient(180deg, #ffffff 30%, #94a3b8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .hero-desc {{
            font-size: 1.15rem;
            color: var(--text-sec);
            max-width: 660px;
            margin: 0 auto 36px;
            line-height: 1.6;
        }}

        /* Store Badges (Approach B: Launching Soon) */
        .store-buttons {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 18px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }}

        .store-btn {{
            position: relative;
            display: inline-flex;
            align-items: center;
            gap: 14px;
            padding: 13px 26px;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            color: #ffffff;
            text-decoration: none;
            transition: all 0.25s ease;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
            cursor: pointer;
        }}

        .store-btn:hover {{
            border-color: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 12px 30px var(--primary-glow);
        }}

        .store-btn svg {{
            width: 28px;
            height: 28px;
            flex-shrink: 0;
        }}

        .store-btn-text {{
            text-align: left;
            line-height: 1.2;
        }}

        .store-btn-small {{
            display: block;
            font-size: 0.68rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-sec);
            font-weight: 600;
        }}

        .store-btn-large {{
            display: block;
            font-size: 1.15rem;
            font-weight: 700;
            letter-spacing: -0.01em;
        }}

        .status-badge {{
            position: absolute;
            top: -10px;
            right: 12px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #ffffff;
            font-size: 0.68rem;
            font-weight: 700;
            padding: 3px 9px;
            border-radius: 999px;
            letter-spacing: 0.04em;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
        }}

        .hero-subnote {{
            font-size: 0.86rem;
            color: var(--text-muted);
            margin-top: 14px;
        }}

        .hero-subnote a {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
        }}

        .hero-subnote a:hover {{
            text-decoration: underline;
        }}

        /* Section Headers */
        .section-title {{
            text-align: center;
            font-size: 2.1rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin-bottom: 12px;
            color: #ffffff;
        }}

        .section-desc {{
            text-align: center;
            max-width: 620px;
            margin: 0 auto 46px;
            color: var(--text-sec);
            font-size: 1rem;
        }}

        /* Features Grid */
        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 22px;
            margin-bottom: 85px;
        }}

        .feature-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 30px 26px;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }}

        .feature-card:hover {{
            transform: translateY(-4px);
            border-color: var(--border-hover);
            box-shadow: 0 14px 34px rgba(0, 0, 0, 0.45);
        }}

        .feature-icon-wrapper {{
            width: 52px;
            height: 52px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 18px;
            font-size: 1.6rem;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border);
        }}

        .feature-title {{
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 10px;
            color: #ffffff;
        }}

        .feature-text {{
            color: var(--text-sec);
            font-size: 0.94rem;
            line-height: 1.55;
        }}

        /* Screenshots Carousel */
        .screenshots-section {{
            padding: 20px 0 85px;
        }}

        .screenshots-scroll {{
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding: 18px 4px 28px;
            scroll-snap-type: x mandatory;
            -webkit-overflow-scrolling: touch;
        }}

        .screenshots-scroll::-webkit-scrollbar {{
            height: 8px;
        }}

        .screenshots-scroll::-webkit-scrollbar-track {{
            background: var(--surface);
            border-radius: 999px;
        }}

        .screenshots-scroll::-webkit-scrollbar-thumb {{
            background: rgba(255, 255, 255, 0.2);
            border-radius: 999px;
        }}

        .screenshot-item {{
            flex: 0 0 auto;
            width: 250px;
            scroll-snap-align: center;
            border-radius: 22px;
            overflow: hidden;
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.55);
            border: 1px solid var(--border);
            transition: transform 0.3s, border-color 0.3s;
        }}

        .screenshot-item:hover {{
            transform: scale(1.02);
            border-color: var(--border-hover);
        }}

        .screenshot-item img {{
            width: 100%;
            height: auto;
            display: block;
        }}

        /* Support & Contact Section */
        .support-box {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 42px 36px;
            margin-bottom: 85px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            align-items: center;
        }}

        @media (max-width: 768px) {{
            .support-box {{
                grid-template-columns: 1fr;
                gap: 28px;
                padding: 30px 22px;
            }}
        }}

        .support-left h3 {{
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 12px;
            color: #ffffff;
        }}

        .support-left p {{
            color: var(--text-sec);
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 24px;
        }}

        .btn-support {{
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #ffffff;
            padding: 12px 26px;
            border-radius: 14px;
            font-weight: 600;
            text-decoration: none;
            box-shadow: 0 6px 18px var(--primary-glow);
            transition: transform 0.2s;
        }}

        .btn-support:hover {{
            transform: translateY(-2px);
        }}

        .btn-copy {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border);
            color: var(--text);
            padding: 12px 20px;
            border-radius: 14px;
            font-weight: 600;
            cursor: pointer;
            margin-left: 12px;
            transition: all 0.2s;
        }}

        .btn-copy:hover {{
            border-color: var(--primary);
            background: rgba(255, 255, 255, 0.1);
        }}

        /* FAQ Accordion */
        .faq-list {{
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}

        .faq-item {{
            background: var(--surface-elevated);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px 22px;
        }}

        .faq-question {{
            font-weight: 600;
            font-size: 1rem;
            color: #ffffff;
            margin-bottom: 8px;
        }}

        .faq-answer {{
            color: var(--text-sec);
            font-size: 0.92rem;
            line-height: 1.5;
        }}

        /* Legal / Privacy / Terms Cards */
        .legal-section {{
            margin-bottom: 90px;
        }}

        .info-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 36px 32px;
            margin-bottom: 30px;
        }}

        .info-card h3 {{
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 16px;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .badge-inline {{
            font-size: 0.72rem;
            padding: 3px 10px;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border);
            border-radius: 999px;
            color: var(--primary);
            font-weight: 600;
        }}

        .info-card h4 {{
            font-size: 1.15rem;
            font-weight: 700;
            color: #ffffff;
            margin: 22px 0 8px;
        }}

        .info-card p {{
            color: var(--text-sec);
            font-size: 0.95rem;
            line-height: 1.65;
            margin-bottom: 12px;
        }}

        .info-card ul {{
            padding-left: 22px;
            color: var(--text-sec);
            font-size: 0.95rem;
            line-height: 1.65;
            margin-bottom: 16px;
        }}

        .info-card li {{
            margin-bottom: 8px;
        }}

        .info-card a {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
        }}

        .info-card a:hover {{
            text-decoration: underline;
        }}

        /* Footer */
        footer {{
            border-top: 1px solid var(--border);
            padding: 40px 0;
            text-align: center;
            background: rgba(7, 9, 14, 0.95);
        }}

        .footer-links {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 22px;
            list-style: none;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }}

        .footer-links a {{
            color: var(--text-sec);
            text-decoration: none;
            font-size: 0.92rem;
            transition: color 0.2s;
        }}

        .footer-links a:hover {{
            color: var(--text);
        }}

        footer p {{
            color: var(--text-muted);
            font-size: 0.88rem;
        }}

        /* Interactive Early Access Modal (Approach B) */
        .modal-backdrop {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(3, 5, 8, 0.82);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            z-index: 1000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}

        .modal-backdrop.is-active {{
            display: flex;
        }}

        .modal-card {{
            background: #0f131d;
            border: 1px solid var(--border);
            border-radius: 24px;
            max-width: 540px;
            width: 100%;
            padding: 36px 32px;
            position: relative;
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.7);
            animation: modalFadeIn 0.25s ease-out;
        }}

        @keyframes modalFadeIn {{
            from {{ opacity: 0; transform: scale(0.95) translateY(10px); }}
            to {{ opacity: 1; transform: scale(1) translateY(0); }}
        }}

        .modal-close {{
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255, 255, 255, 0.08);
            border: none;
            width: 34px;
            height: 34px;
            border-radius: 50%;
            color: #ffffff;
            font-size: 1.3rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
        }}

        .modal-close:hover {{
            background: rgba(255, 255, 255, 0.16);
        }}

        .modal-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--primary);
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border);
            padding: 5px 14px;
            border-radius: 999px;
            margin-bottom: 14px;
        }}

        .modal-title {{
            font-size: 1.8rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 10px;
            letter-spacing: -0.02em;
        }}

        .modal-subtitle {{
            color: var(--text-sec);
            font-size: 0.95rem;
            line-height: 1.55;
            margin-bottom: 26px;
        }}

        .modal-steps {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .step-card {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px;
            display: flex;
            gap: 16px;
            align-items: flex-start;
        }}

        .step-number {{
            width: 32px;
            height: 32px;
            background: var(--primary);
            color: #ffffff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 0.92rem;
            flex-shrink: 0;
            box-shadow: 0 4px 12px var(--primary-glow);
        }}

        .step-content h4 {{
            font-size: 1.05rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 4px;
        }}

        .step-content p {{
            color: var(--text-sec);
            font-size: 0.9rem;
            line-height: 1.45;
            margin-bottom: 14px;
        }}

        .btn-step {{
            display: inline-block;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #ffffff;
            padding: 9px 18px;
            border-radius: 10px;
            font-size: 0.88rem;
            font-weight: 600;
            text-decoration: none;
            box-shadow: 0 4px 12px var(--primary-glow);
            transition: transform 0.2s;
        }}

        .btn-step:hover {{
            transform: translateY(-2px);
        }}

        .btn-step-sec {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border);
            box-shadow: none;
            color: var(--text);
            cursor: pointer;
        }}

        .btn-step-sec:hover {{
            background: rgba(255, 255, 255, 0.14);
        }}
    </style>
</head>
<body>
    <div class="ambient-bg"></div>

    <!-- Navigation -->
    <nav>
        <div class="container nav-content">
            <a href="#" class="logo">
                <img src="{icon}" alt="{name} Icon">
                <span>{name}</span>
            </a>
            <ul class="nav-links">
                <li><a href="#features">Features</a></li>
                {screenshots_nav}
                <li><a href="#support">Support</a></li>
                <li><a href="#privacy">Privacy</a></li>
                <li><a href="#terms">Terms</a></li>
                <li><a href="#early-access" class="nav-cta" onclick="openEarlyAccessModal(event)">Get Early Access</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="container">
        <!-- Hero Section -->
        <section class="hero" id="download">
            <div class="badge-pill">
                <span>{badge}</span>
            </div>

            <img src="{icon}" alt="{name} App Icon" class="hero-icon">

            <span class="hero-tagline">{tagline}</span>
            <h1>{name}</h1>
            <p class="hero-desc">{hero_desc}</p>

            <!-- Store Badges (Approach B: Launching Soon) -->
            <div class="store-buttons">
                <!-- Apple App Store (Coming Soon) -->
                <a href="#early-access" class="store-btn" id="btn-ios" onclick="openEarlyAccessModal(event)">
                    <span class="status-badge">Launching Soon</span>
                    <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.37c.61-.75 1.04-1.8 0.92-2.87-.93.04-2.02.63-2.67 1.38-.56.65-.96 1.71-.83 2.74 1.03.08 2.05-.53 2.58-1.25z"/>
                    </svg>
                    <div class="store-btn-text">
                        <span class="store-btn-small">COMING SOON TO</span>
                        <span class="store-btn-large">App Store</span>
                    </div>
                </a>

                <!-- Google Play Store (Coming Soon) -->
                <a href="#early-access" class="store-btn" id="btn-android" onclick="openEarlyAccessModal(event)">
                    <span class="status-badge">Launching Soon</span>
                    <svg viewBox="0 0 24 24">
                        <path fill="#4285F4" d="M3.6 2.5l9.2 9.2-9.2 9.2c-.3-.4-.5-.9-.5-1.5V4c0-.6.2-1.1.5-1.5z"/>
                        <path fill="#FBBC04" d="M16.6 9.3l-3.8 3.8 3.8 3.8 4.3-2.5c1.2-.7 1.2-1.9 0-2.6l-4.3-2.5z"/>
                        <path fill="#34A853" d="M3.6 21l9.2-9.2 3.8 3.8-10.8 6.2c-.8.5-1.7.3-2.2-.8z"/>
                        <path fill="#EA4335" d="M3.6 2.5c.5-1.1 1.4-1.3 2.2-.8L16.6 8 12.8 11.7 3.6 2.5z"/>
                    </svg>
                    <div class="store-btn-text">
                        <span class="store-btn-small">COMING SOON TO</span>
                        <span class="store-btn-large">Google Play</span>
                    </div>
                </a>
            </div>

            <p class="hero-subnote">
                Want early beta access? <a href="#early-access" onclick="openEarlyAccessModal(event)">Request an invitation &rarr;</a>
            </p>
        </section>

        <!-- Features Section -->
        <section id="features">
            <h2 class="section-title">Engineered for Excellence</h2>
            <p class="section-desc">Key highlights that make {name} special, focused, and intuitive.</p>

            <div class="features-grid">
                {features_html}
            </div>
        </section>

        {screenshots_section}

        <!-- Support Section -->
        <section id="support">
            <div class="support-box">
                <div class="support-left">
                    <h3>💬 Dedicated Support</h3>
                    <p>Have an inquiry, feedback, or a feature request? Our development team personally reviews every message.</p>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center;">
                        <a href="mailto:{email}?subject={name}%20Inquiry" class="btn-support">✉️ Contact Developer</a>
                        <button class="btn-copy" onclick="copySupportEmail('{email}')" id="copyBtn">📋 Copy Email</button>
                    </div>
                </div>
                <div class="faq-list">
                    {faqs_html}
                </div>
            </div>
        </section>

        <!-- Privacy & Terms Legal Section -->
        <section class="legal-section" id="privacy">
            <div class="info-card">
                <h3>🔒 Privacy Policy <span class="badge-inline">GDPR • COPPA • CalOPPA</span></h3>
                <p><strong>Last Updated: October 2026</strong></p>
                <p>Your privacy is paramount. <strong>{name}</strong> is built strictly around local-first privacy principles. We believe your personal tools should never monitor, track, or commercialize your identity.</p>

                <h4>1. Information Collection & Use</h4>
                <p>{privacy_clause_1}</p>

                <h4>2. On-Device Storage & Local Operation</h4>
                <p>All core settings, user progress, customized preferences, and app states are stored strictly within sandboxed storage on your local device. We run zero remote database synchronization services that profile individual user habits.</p>

                <h4>3. Third-Party Services & Analytics</h4>
                <p>{privacy_clause_3}</p>

                <h4>4. Children’s Privacy (COPPA Compliance)</h4>
                <p>We are firmly committed to safeguarding the privacy of young users. {name} does not knowingly collect personally identifiable information from children under 13. Any features tailored for younger audiences strictly respect international child protection regulations.</p>

                <h4>5. Contact Us</h4>
                <p>For any privacy or data protection inquiries, email our privacy team directly at: <a href="mailto:{email}">{email}</a>.</p>
            </div>

            <div class="info-card" id="terms">
                <h3>📄 Terms of Service <span class="badge-inline">EULA</span></h3>
                <p><strong>Last Updated: October 2026</strong></p>
                <p>By downloading, previewing, or using <strong>{name}</strong>, you agree to these Terms of Service in conjunction with standard Apple Media Services and Google Play Terms.</p>

                <h4>1. License Grant</h4>
                <p>We grant you a personal, revocable, non-exclusive, non-transferable license to install and use {name} on any authorized iOS or Android device you own or control.</p>

                <h4>2. Intellectual Property</h4>
                <p>All trademarks, user interface designs, visual layouts, soundscapes, source code, and assets associated with {name} remain the exclusive property of the developer. You may not decompile, reverse-engineer, or redistribute the application without express written consent.</p>

                <h4>3. In-App Purchases (If Applicable)</h4>
                <p>Any digital unlocks (such as a Lifetime Pass) are billed through official Apple App Store or Google Play Console in-app billing engines. All transactions, refunds, and family sharing are governed by the respective platform terms.</p>

                <h4>4. Disclaimer of Warranties</h4>
                <p>{name} is provided on an "as-is" and "as-available" basis. While we strive for uncompromising stability and precision, the developer disclaims all warranties to the maximum extent permitted by applicable law.</p>

                <h4>5. Governing Law & Support</h4>
                <p>For questions regarding these Terms or legal support, contact: <a href="mailto:{email}">{email}</a>.</p>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <ul class="footer-links">
                <li><a href="#download">Early Access</a></li>
                <li><a href="#features">Features</a></li>
                {screenshots_footer}
                <li><a href="#support">Support</a></li>
                <li><a href="#privacy">Privacy Policy</a></li>
                <li><a href="#terms">Terms</a></li>
                <li><a href="app-ads.txt" target="_blank">app-ads.txt</a></li>
            </ul>
            <p>&copy; 2026 {name}. All rights reserved.</p>
            <p style="margin-top: 6px; font-size: 0.8rem; color: var(--text-muted);">Coming Soon to Apple App Store & Google Play • Privacy-First Architecture</p>
        </div>
    </footer>

    <!-- Interactive Early Access Modal (Approach B) -->
    <div id="earlyAccessModal" class="modal-backdrop" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
        <div class="modal-card">
            <button class="modal-close" onclick="closeEarlyAccessModal()" aria-label="Close modal">&times;</button>
            <div class="modal-header">
                <div class="modal-badge">
                    <span>🚀 Pre-Launch Early Access</span>
                </div>
                <h3 id="modalTitle" class="modal-title">Get Early Access to {name}</h3>
                <p class="modal-subtitle">{name} is currently in active development for Apple iOS and Android. Request a closed beta invitation or get notified the exact hour we launch on the App Store and Google Play.</p>
            </div>

            <div class="modal-steps">
                <div class="step-card">
                    <div class="step-number">1</div>
                    <div class="step-content">
                        <h4>Request Closed Beta Invitation</h4>
                        <p>Join our private Apple TestFlight or Google Play closed testing track to try {name} before the general public.</p>
                        <a href="mailto:{email}?subject=Early%20Access%20Request%20-%20{name}&body=Hi%20Saad,%0D%0A%0D%0AI%20would%20like%20to%20request%20early%20beta%20access%20to%20{name}.%0D%0A%0D%0APlatform:%20(iOS%20/%20Android)%0D%0AEmail:%20" class="btn-step" target="_blank">✉️ Request Beta Invite</a>
                    </div>
                </div>

                <div class="step-card">
                    <div class="step-number">2</div>
                    <div class="step-content">
                        <h4>Direct Developer Inquiries</h4>
                        <p>Have custom questions or partnership inquiries? Feel free to copy our direct developer email.</p>
                        <button type="button" class="btn-step btn-step-sec" onclick="copySupportEmail('{email}')">📋 Copy Support Email</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Interactive Scripts -->
    <script>
        function openEarlyAccessModal(e) {{
            if (e) {{
                e.preventDefault();
                e.stopPropagation();
            }}
            const modal = document.getElementById('earlyAccessModal');
            if (modal) {{
                modal.classList.add('is-active');
                document.body.style.overflow = 'hidden';
            }}
            return false;
        }}

        function closeEarlyAccessModal() {{
            const modal = document.getElementById('earlyAccessModal');
            if (modal) {{
                modal.classList.remove('is-active');
                document.body.style.overflow = '';
            }}
        }}

        window.addEventListener('click', function(e) {{
            const modal = document.getElementById('earlyAccessModal');
            if (modal && e.target === modal) {{
                closeEarlyAccessModal();
            }}
        }});

        window.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                closeEarlyAccessModal();
            }}
        }});

        function copySupportEmail(email) {{
            navigator.clipboard.writeText(email).then(() => {{
                const btns = document.querySelectorAll('#copyBtn, .btn-step-sec');
                btns.forEach(btn => {{
                    const orig = btn.innerText;
                    btn.innerText = '✓ Email Copied!';
                    setTimeout(() => {{ btn.innerText = orig; }}, 2500);
                }});
            }}).catch(() => {{
                prompt('Copy Developer Email:', email);
            }});
        }}
    </script>
</body>
</html>
"""

def generate_page(app_key, data):
    base_dir = "/Users/saad/Documents/Rj707.github.io"
    app_dir = os.path.join(base_dir, app_key)
    os.makedirs(app_dir, exist_ok=True)
    
    # 1. Features HTML
    features_html = ""
    for f in data["features"]:
        features_html += f"""
                <div class="feature-card">
                    <div class="feature-icon-wrapper">{f['icon']}</div>
                    <h3 class="feature-title">{f['title']}</h3>
                    <p class="feature-text">{f['text']}</p>
                </div>"""
        
    # 2. FAQs HTML
    faqs_html = ""
    for q, a in data["faqs"]:
        faqs_html += f"""
                    <div class="faq-item">
                        <div class="faq-question">❓ {q}</div>
                        <div class="faq-answer">{a}</div>
                    </div>"""
        
    # 3. Screenshots Section
    has_screenshots = len(data["screenshots"]) > 0
    if has_screenshots:
        screenshots_nav = '<li><a href="#screenshots">Screenshots</a></li>'
        screenshots_footer = '<li><a href="#screenshots">Screenshots</a></li>'
        items_html = ""
        for img, alt in data["screenshots"]:
            items_html += f"""
                <div class="screenshot-item">
                    <img src="screenshots/{img}" alt="{alt}" loading="lazy">
                </div>"""
            
        screenshots_section = f"""
        <!-- Screenshots Showcase -->
        <section class="screenshots-section" id="screenshots">
            <h2 class="section-title">Visual Showcase</h2>
            <p class="section-desc">Swipe through high-resolution captures of {data['name']} in action.</p>

            <div class="screenshots-scroll">
                {items_html}
            </div>
        </section>"""
    else:
        screenshots_nav = ""
        screenshots_footer = ""
        screenshots_section = ""

    # 4. Privacy clauses tailored
    if data["legal_type"] == "kids":
        p1 = f"{data['name']} is engineered specifically with family and child safety at its core. We do not require account registration, do not collect names, addresses, or phone numbers, and do not track individual child behavior."
        p3 = f"{data['name']} operates strictly within child-safe boundaries. It does not integrate behavioral ad networks, and any in-app tools strictly adhere to Google Play Families and Apple Kids categories."
    elif data["legal_type"] == "utility":
        p1 = f"{data['name']} does NOT collect, store, or transmit personally identifiable information (PII). All user-created timers, presets, soundscape mixes, and focus streaks remain 100% on-device."
        p3 = f"Any telemetry, if enabled, is strictly non-identifying crash reporting (e.g. Firebase Crashlytics) used exclusively to resolve bugs and device compatibility issues."
    elif data["legal_type"] == "family":
        p1 = f"We treat your family's personal milestones with sacred trust. {data['name']} never sells, rents, or commercializes baby growth measurements, diaper logs, feeding times, or personal photos."
        p3 = "Data synchronization between authorized family members uses encrypted, direct platform services (Apple iCloud / Google Cloud) and is never accessible to third-party data brokers."
    else:
        p1 = f"{data['name']} does not collect personal identity information, passwords, or contacts. You can use all core functions completely anonymously."
        p3 = "Non-personalized analytics and crash telemetry may be used to identify software errors and optimize frame rates across different device specifications."

    html_content = HTML_TEMPLATE.format(
        title=data["title"],
        name=data["name"],
        slug=data["slug"],
        tagline=data["tagline"],
        badge=data["badge"],
        hero_desc=data["hero_desc"],
        icon=data["icon"],
        primary_color=data["primary_color"],
        accent_color=data["accent_color"],
        glow_color=data["glow_color"],
        email=data["email"],
        features_html=features_html,
        faqs_html=faqs_html,
        screenshots_nav=screenshots_nav,
        screenshots_footer=screenshots_footer,
        screenshots_section=screenshots_section,
        privacy_clause_1=p1,
        privacy_clause_3=p3
    )
    
    out_file = os.path.join(app_dir, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated modern page for {data['name']} -> {out_file}")

    # Ensure app-ads.txt exists in app folder or symlink
    app_ads_file = os.path.join(app_dir, "app-ads.txt")
    if not os.path.exists(app_ads_file):
        with open(app_ads_file, "w") as f:
            f.write("google.com, pub-4042428849777474, DIRECT, f08c47fec0942fa0\n")

    # Backward compatibility redirect for privacy.html & terms.html
    redirect_privacy = os.path.join(app_dir, "privacy.html")
    with open(redirect_privacy, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=index.html#privacy"><title>Privacy Policy</title></head><body><p>Redirecting to <a href="index.html#privacy">Privacy Policy</a>...</p></body></html>')

    redirect_terms = os.path.join(app_dir, "terms.html")
    with open(redirect_terms, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=index.html#terms"><title>Terms of Service</title></head><body><p>Redirecting to <a href="index.html#terms">Terms of Service</a>...</p></body></html>')

    redirect_support = os.path.join(app_dir, "support.html")
    with open(redirect_support, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=index.html#support"><title>Support</title></head><body><p>Redirecting to <a href="index.html#support">Support</a>...</p></body></html>')

def main():
    for app_key, data in APPS.items():
        generate_page(app_key, data)

if __name__ == "__main__":
    main()

# BonfireNightUK.co.uk — Project Brief

You are designing a UK authority website called BonfireNightUK.co.uk.

This is NOT a startup app.
It is a seasonal national reference site for Bonfire Night events.

Positioning:
"The trusted UK guide to Bonfire Night events."
British. Clean. Established. Not gimmicky. Not tech-bro.

Primary objective:
Build a simple, SEO-first, self-serve marketplace that:
- Lists Bonfire Night events across UK cities
- Allows organisers to submit events
- Offers paid featured listings (£99–£199)
- Runs automatically each year
- Requires minimal maintenance outside Sept–Nov

Do NOT add feature creep.
Do NOT add dashboards, gamification, chatbots, social feeds or complex analytics.

----------------------------------------------------
PUBLIC SITE STRUCTURE
----------------------------------------------------

1) HOMEPAGE

Headline:
"Find Bonfire Night Events Near You"

Must include:
- Postcode search
- Top UK city quick links
- Email capture ("Get notified when 2027 events go live near you")
- Clear CTA: "Submit Your Event"

Design style:
- Navy / deep red / off-white
- Clean typography
- Trustworthy British tone
- No playful or childish elements

----------------------------------------------------

2) CITY SEO PAGES (CORE GROWTH ENGINE)

Example URL:
 /manchester-bonfire-night-2026

Each page must include:
- 200–300 word SEO-optimised introduction
- Event listings (Featured first)
- Safety reminder section
- FAQ
- Internal links to Safety Hub
- "Submit your event" CTA

These pages are the primary ranking asset.

----------------------------------------------------

3) EVENT DETAIL PAGE

Each event page includes:
- Event name
- Date & time
- Location + map
- Description
- Ticket link
- Image
- Tags (Family-friendly, Food available, etc.)
- Featured badge if paid
- Structured Event schema markup

Optional later: ratings (NOT in MVP).

----------------------------------------------------

4) SAFETY & LAW HUB (TRUST BUILDER)

Create static authority pages:

- Firework laws in the UK
- When can fireworks legally be set off?
- Firework curfew times
- F1–F4 categories explained
- Pet safety advice

Purpose:
- Increase SEO authority
- Build trust
- Reduce liability perception

----------------------------------------------------

EMAIL SYSTEM (CRITICAL ASSET)

- Capture email + postcode
- Tag by region
- Store for annual reminder
- No newsletters in MVP
- Use list as yearly traffic trigger

----------------------------------------------------
ORGANISER SIDE (SELF-SERVE ONLY)
----------------------------------------------------

Keep simple. No complexity.

1) Account creation
2) Submit event form:
   - Name
   - Date
   - Location
   - Description
   - Ticket URL
   - Image upload
3) Free listing by default
4) Upgrade to Featured (£149)
   - Stripe payment
   - Automatic upgrade

----------------------------------------------------

AUTOMATION RULES (MANDATORY)

- All events automatically expire on November 6
- Events status changes to expired automatically
- Organisers receive automatic renewal email on August 1 next year
- No manual moderation in MVP

This must run automatically with scheduled jobs.

----------------------------------------------------

DATABASE REQUIREMENTS

Entities:
- Users (organisers)
- Events
- Cities
- Payments
- Email subscribers

Events must include:
- featured (boolean)
- expires_at (datetime)
- status (active/expired)
- city reference
- year reference (2026, 2027, etc.)

Structure must support reuse each year without redesign.

----------------------------------------------------

MONETISATION MODEL (MVP ONLY)

1) Featured listings (£99–£199)
2) Affiliate links (optional)
3) Optional display ads

No other revenue streams in Year 1.

----------------------------------------------------

IMPORTANT CONSTRAINTS

- Must feel like a national reference site.
- Must prioritise SEO structure.
- Must minimise long-term manual effort.
- Must be fully usable by September 2026.
- Avoid adding features not directly tied to revenue, SEO, or automation.

Remember:
This is a seasonal authority asset.
Not a hobby.
Not a tech experiment.

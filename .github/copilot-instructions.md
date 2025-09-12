## Quick orientation for AI coding agents

This repo is a Streamlit-based website for the CCSC organization. Keep instructions short, precise, and keyed to files below so contributors can be immediately productive.

- Project entry: `main.py` — the Streamlit app entrypoint. Launch locally with: `pip install -r requirements.txt` then `streamlit run main.py`.
- Pages: the `pages/` folder holds individual Streamlit pages (e.g. `pages/about_us.py`, `pages/activities.py`). Each page imports `init_page` from `utils` and relies on `st.sidebar.page_link` for navigation.
- Common utilities: `utils/utils.py` and `utils/menu.py` provide page initialization and menu wiring. Prefer adding shared helpers here rather than ad-hoc imports across pages.
- Static assets: `static/images/` stores logos and banners used by pages. Use relative paths like `static/images/logo.png` when referencing images via Streamlit or components.

Rules for edits
- Keep public API surface stable: avoid renaming `init_page` or `menu` functions without updating all `pages/*` imports.
- Prefer small, focused changes: modify one page or util at a time and run `streamlit run main.py` to validate visual output.

Patterns and examples
- Page initialization: call `init_page(page_name="about_us")` at the top of a page to set title and nav state (see `pages/about_us.py`).
- Styling: many pages use `st.markdown(..., unsafe_allow_html=True)` and `components.html(...)` for custom HTML/CSS. Preserve this pattern if you need bespoke layouts.
- Session state: pages rely on `st.session_state.page_name`; use `st.session_state` to share lightweight state across pages.

Developer workflows
- Install deps: `pip install -r requirements.txt` (file lists Streamlit pinned version).
- Run locally: `streamlit run main.py` — app serves at http://localhost:8501 by default.
- Quick visual check: modify one page, run the app, use browser refresh. There is no automated test suite in the repo.

Integration points & constraints
- No database or external API is present in the codebase; pages are static content modules. If adding integrations, include configuration via `.env` and `python-dotenv`.
- Avoid adding heavy async or background services—Streamlit is single-process; prefer synchronous code for UI rendering.

Files to inspect when making changes
- `main.py`, `utils/utils.py`, `utils/menu.py`, and any file under `pages/` relevant to your change. Use `static/images/` for image assets.

If you need more context
- Ask the repo owner which pages are canonical for content (e.g. `about_us`, `calendar`, `activities`) before refactoring layout or navigation.

Feedback request: I wrote this based on the repository structure and README. Tell me which parts are unclear or what additional examples you want included.

import streamlit as st
import os


def _valid_icon(icon) -> bool:
    # Accept any non-empty string that is not a shortcode like :smile:
    if icon is None:
        return False
    try:
        s = str(icon).strip()
    except Exception:
        return False
    if s == "":
        return False
    # reject shortcodes of the form :name:
    if s.startswith(":") and s.endswith(":"):
        return False
    return True


def _safe_page_link(page, label: str, icon=None):
    """Render a sidebar link.

    - If the label is indented (starts with NBSP), we include the icon inside the label
      and call page_link without the `icon=` parameter so the icon respects indentation.
    - For top-level labels, we prefer passing the `icon=` parameter so Streamlit renders
      the icon in its native widget.
    - We avoid producing markdown-list bullets; fallbacks use inline HTML with no underline.
    """
    try:
        valid = _valid_icon(icon)
        is_indented = isinstance(label, str) and label.startswith("\u00a0")

        # If this is an indented sublabel, insert the icon after the indent so it aligns.
        if is_indented:
            # count leading NBSPs to preserve indentation
            nb_count = len(label) - len(label.lstrip("\u00a0"))
            indent_prefix = "\u00a0" * nb_count
            core_label = label.lstrip("\u00a0")
            label_with_icon = f"{indent_prefix}{icon} {core_label}" if valid else label
            try:
                st.sidebar.page_link(page, label=label_with_icon)
                return
            except Exception:
                # fallback: try without icon inserted
                try:
                    st.sidebar.page_link(page, label=label)
                    return
                except Exception:
                    pass

        # Non-indented (top-level)
        if valid:
            # Try native icon param first
            try:
                st.sidebar.page_link(page, label=label, icon=icon)
                return
            except Exception:
                # If that fails, put icon in label and call without icon param
                try:
                    label_with_icon = f"{icon} {label}"
                    st.sidebar.page_link(page, label=label_with_icon)
                    return
                except Exception:
                    pass
        else:
            try:
                st.sidebar.page_link(page, label=label)
                return
            except Exception:
                pass

        # As a last resort, render an inline HTML anchor without underline (best-effort)
        try:
            # compute indent pixels from NBSP count if present
            nb_count = 0
            if isinstance(label, str):
                nb_count = len(label) - len(label.lstrip("\u00a0"))
            indent_px = max(0, nb_count * 4)

            icon_html = icon if valid else ""
            # Create a fixed-width span for icon so icons align across rows
            icon_span = f'<span style="display:inline-block; width:28px; text-align:left; margin-left:{indent_px}px">{icon_html}</span>'
            # core text without NBSP prefix for HTML rendering
            core_text = label.lstrip("\u00a0") if isinstance(label, str) else label
            html = (
                f'<div style="padding:4px 0; display:flex; align-items:center">'
                f'{icon_span}<a href="#" style="text-decoration:none; color:inherit;">{core_text}</a></div>'
            )
            st.sidebar.markdown(html, unsafe_allow_html=True)
            return
        except Exception:
            # final silent fallback: plain text
            try:
                st.sidebar.markdown(label)
            except Exception:
                pass
    except Exception:
        try:
            st.sidebar.markdown(label)
        except Exception:
            pass


def _section_of(page_name: str) -> str:
    """Map a page_name to its top-level section.

    Normalize page_name by extracting the basename (file name) and lowercasing,
    then check for known section keywords. This handles values like
    'pages/about_us_what_is_ccsc.py', 'about_us_vision_ccsc', or 'about_us'.
    """
    if not page_name:
        return "home"
    try:
        # If page_name looks like a path, get the filename; else use as-is
        base = os.path.basename(str(page_name))
        # remove extension if present
        base = os.path.splitext(base)[0]
        s = base.lower()
    except Exception:
        s = str(page_name).lower()

    # Check sections by keyword presence (order matters for specificity)
    if "about_us" in s or s.startswith("about"):
        return "about_us"
    if "activities" in s or s.startswith("activities"):
        return "activities"
    if "serviceslife" in s or s.startswith("services"):
        return "serviceslife"
    if "calendar" in s:
        return "calendar"
    if "publications" in s or s.startswith("publications"):
        return "publications"
    if "search" in s:
        return "search"
    if s == "home" or s == "main":
        return "home"
    # default: treat as home (show top-level)
    return "home"


def _indent_label(label: str, level: int = 1) -> str:
    """Return a label prefixed with non-breaking spaces to create visual indentation."""
    return ("\u00a0" * 4 * level) + label


def menu():
    st.sidebar.title("導航")
    current_page = st.session_state.get("page_name", "home")
    section = _section_of(current_page)

    entries = []

    if section == "home":
        # show all top-level links
        entries = [
            ("main.py", "首頁", "✝️"),
            ("pages/about_us.py", "關於我們", "👨‍👩‍👧‍👦"),
            ("pages/activities.py", "活動訊息", "🎯"),
            ("pages/serviceslife.py", "服務與生活", "🛠️"),
            ("pages/calendar.py", "行事曆", "📅"),
            ("pages/publications.py", "小會刊物", "📚"),
            ("pages/search.py", "搜尋", "🔍"),
        ]
    else:
        # Non-home sections: always provide a link back to homepage first
        entries.append(("main.py", "返回首頁", "✝️"))

        if section == "about_us":
            entries.extend(
                [
                    ("pages/about_us.py", "關於我們", "👨‍👩‍👧‍👦"),
                    (
                        "pages/about_us_what_is_ccsc.py",
                        _indent_label("小會是甚麼?", 1),
                        "❓",
                    ),
                    (
                        "pages/about_us_vision_ccsc.py",
                        _indent_label("宗旨與精神", 1),
                        "📜",
                    ),
                    (
                        "pages/about_us_history_ccsc.py",
                        _indent_label("歷史沿革", 1),
                        "✝️",
                    ),
                    (
                        "pages/about_us_timeline_ccsc.py",
                        _indent_label("大事年表", 1),
                        "📅",
                    ),
                ]
            )
        elif section == "activities":
            entries.extend(
                [
                    ("pages/activities.py", "活動訊息", "🎯"),
                    (
                        "pages/activities_head_office.py",
                        _indent_label("總會活動", 1),
                        "🎯",
                    ),
                    (
                        "pages/activities_taipei_branch.py",
                        _indent_label("台北分會活動", 1),
                        "🎯",
                    ),
                    (
                        "pages/activities_taichung_branch.py",
                        _indent_label("台中分會活動", 1),
                        "📋",
                    ),
                    (
                        "pages/activities_kaohsiung_branch.py",
                        _indent_label("高雄分會活動", 1),
                        "📅",
                    ),
                    (
                        "pages/activities_northamerica_branch.py",
                        _indent_label("北美分會活動", 1),
                        "📊",
                    ),
                ]
            )
        elif section == "serviceslife":
            entries.extend(
                [
                    ("pages/serviceslife.py", "服務與生活", "🛠️"),
                    (
                        "pages/serviceslife_culture_spread.py",
                        _indent_label("文化福傳", 1),
                        None,
                    ),
                ]
            )
        elif section == "calendar":
            entries.extend(
                [
                    ("pages/calendar.py", "行事曆", "📅"),
                    (
                        "pages/calendar_head_office.py",
                        _indent_label("總會行事曆", 1),
                        "📅",
                    ),
                    (
                        "pages/calendar_taipei_branch.py",
                        _indent_label("台北分會行事曆", 1),
                        "📅",
                    ),
                    (
                        "pages/calendar_taichung_branch.py",
                        _indent_label("台中分會行事曆", 1),
                        "📅",
                    ),
                    (
                        "pages/calendar_kaohsiung_branch.py",
                        _indent_label("高雄分會行事曆", 1),
                        "📅",
                    ),
                    (
                        "pages/calendar_northamerica_branch.py",
                        _indent_label("北美分會行事曆", 1),
                        "📅",
                    ),
                ]
            )
        elif section == "publications":
            entries.extend(
                [
                    # ("pages/publications.py", "小會刊物", "📚"),
                    # (
                    #    "pages/publications_wellspring.py",
                    #    _indent_label("心泉文章", 1),
                    #    "💧",
                    # ),
                    (
                        "pages/publications_wellspring_gdrive.py",
                        _indent_label("心泉", 1),
                        "💧",
                    ),
                    (
                        "pages/publications_mustard_seed.py",
                        _indent_label("芥子", 1),
                        "🌱",
                    ),
                ]
            )
        elif section == "search":
            entries.append(("pages/search.py", "搜尋", "🔍"))

    # Render entries while avoiding duplicates
    seen = set()
    for page, label, icon in entries:
        if page in seen:
            continue
        _safe_page_link(page, label=label, icon=icon)
        seen.add(page)

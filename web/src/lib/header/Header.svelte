<script lang="ts">
    import {page} from '$app/stores';
    import {assets, base} from '$app/paths'
    import {default_scorecard_path, pathname_pattern} from "$lib/pathnames.js";
    import BodyContentContainer from "$lib/BodyContentContainer.svelte";

    let nav_checkbox;
    const hide_nav = () => nav_checkbox.checked = false;
</script>

<header class="col-span-4 font-mono items-center fullnav:border-b border-brand-primary-green z-10">
    <BodyContentContainer>
        <div class="flex w-full justify-between fullnav:justify-start mx-auto">
            <input type="checkbox" id="open-mobile-menu" class="hidden" bind:this={nav_checkbox}/>
            <label for="open-mobile-menu" class="flex fullnav:hidden toggle-mobile-menu items-center justify-center p-2"
                   aria-controls="mobile-menu" aria-expanded="false">
                <span class="sr-only">Open main menu</span>
                <svg class="hamburger block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                     stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round"
                          d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/>
                </svg>
                <svg class="cross hidden h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                     stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
                </svg>
            </label>
            <div class="logo flex p-2" on:click={hide_nav}>
                <a href={`${base}/`} class="">
                    <img src={`${assets}/p33-logo.png`} class="h-8 w-8"/>
                </a>
            </div>

            <div class="flex fullnav:hidden h-10 w-10">
                <div></div>
            </div>

            <nav class="hidden fullnav:flex w-full fullnav:w-auto absolute fullnav:static top-12 left-0 right-0 bottom-0 bg-white fullnav:bg-transparent p-4 fullnav:p-0 leading-10 border-t fullnav:border-0 border-brand-primary-green">
                <ul class="fullnav:flex" on:click={hide_nav}>
                    <li class:active={pathname_pattern.test($page.url.pathname)}><a
                            href={`${base}/${default_scorecard_path}`}>Scorecard</a></li>
                    <li class:active={$page.url.pathname === `${base}/methodology`}><a href={`${base}/methodology`}>Methodology</a>
                    </li>
                    <li class:active={$page.url.pathname === `${base}/resources`}><a href={`${base}/resources`}>Resources</a>
                    </li>
                    <li class:active={$page.url.pathname === `${base}/about`}><a href={`${base}/about`}>About Us</a>
                    </li>
                    <li class:active={$page.url.pathname === `${base}/partners`}><a href={`${base}/partners`}>Our
                        Partners</a></li>
                    <li class:active={$page.url.pathname === `${base}/contact`}><a href={`${base}/contact`}>Contact
                        Us</a></li>
                </ul>
            </nav>
        </div>
    </BodyContentContainer>
</header>

<style>
    .logo img {
        filter: invert() brightness(85%) sepia(20%) hue-rotate(120deg);
    }

    :checked ~ .toggle-mobile-menu .hamburger {
        display: none;
    }

    :checked ~ .toggle-mobile-menu .cross {
        display: flex;
    }

    :checked ~ nav {
        display: block;
    }

    nav li {
        padding: 0.25rem 1rem;
    }

    @media screen(lg) {
        .active {
            border-bottom: 2px solid theme('colors.brand-primary-dark-green');
            font-weight: theme('fontWeight.bold');
        }
    }

</style>

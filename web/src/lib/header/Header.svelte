<script lang="ts">
    import {page} from '$app/stores';
    import {assets, base} from '$app/paths'
    import {lifestages} from "../domain/Lifestage.js";
    import {indicators} from "../domain/Indicator";

    let nav_checkbox;
    const hide_nav = () => nav_checkbox.checked = false;
    const dont_hide_nav = () => {};
</script>

<header class="font-mono w-full items-center fullnav:border-b border-brand-primary-green z-10">
    <div class="px-1 md:px-3 lg:px-8 flex justify-between fullnav:justify-start mx-auto max-w-6xl">
        <input type="checkbox" id="open-mobile-menu" class="hidden" bind:this={nav_checkbox}/>
        <label for="open-mobile-menu" class="flex fullnav:hidden toggle-mobile-menu items-center justify-center p-2"
               aria-controls="mobile-menu" aria-expanded="false">
            <span class="sr-only">Open main menu</span>
            <svg class="hamburger block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                 stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/>
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
                <li class:active={$page.url.pathname === `${base}/index`}>
                    <a
                        class="h-full w-full"
                        href={`${base}/index`}>Index</a>
                </li>
                <!-- mobile subnav -->
                {#each lifestages as lifestage}
                    <li class="fullnav:hidden pl-4 pt-1 pb-2">
                        <details class="open:bg-white">
                            <summary class="text-brand-primary-dark-green leading-6 select-none" on:click|capture|stopPropagation={dont_hide_nav}>
                                <span class="leading-8">{lifestage.name}</span>
                                <svg aria-hidden="true" focusable="false" data-prefix="fas" class="inline-block w-3 h-3" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">-->
                                    <path fill="currentColor" d="M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z"></path>
                                </svg>
                            </summary>

                            <div class="mt-3 text-sm leading-6">
                                <ul>
                                    {#each indicators as indicator}
                                        <li><a href={`${base}/${lifestage.route}/${indicator.route}`} class="hover:text-brand-primary-green">{indicator.name}</a></li>
                                    {/each}
                                </ul>
                            </div>
                        </details>
                    </li>
                {/each}
                <li class:active={$page.url.pathname === `${base}/resources`}><a
                        href={`${base}/resources`}>Resources</a></li>
                <li class:active={$page.url.pathname === `${base}/about`}><a href={`${base}/about`}>About Us</a></li>
                <li class:active={$page.url.pathname === `${base}/partners`}><a href={`${base}/partners`}>Our
                    Partners</a></li>
                <li class:active={$page.url.pathname === `${base}/contact`}><a href={`${base}/contact`}>Contact Us</a>
                </li>
            </ul>
        </nav>
    </div>
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

    summary {
        list-style: none;
    }

    details[open] > summary > svg {
        transform: rotate(180deg);
    }

    @media screen(lg) {
        .active {
            border-bottom: 2px solid theme('colors.brand-primary-dark-green');
            font-weight: theme('fontWeight.bold');
        }
    }

</style>
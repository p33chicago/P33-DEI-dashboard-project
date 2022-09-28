<script type="ts">
    import type {Lifestage} from "$lib/domain/Lifestage.ts";
    import type {Indicator} from "$lib/domain/Indicator.ts";
    import {indicators} from "$lib/domain/Indicator.ts";
    import {base} from "$app/paths";

    export let lifestage: Lifestage;
    export let indicator: Indicator;
</script>
<div class="hidden md:block col-start-2 col-span-3 2xl:w-screen space-x-5">
    {#each indicators as _indicator}
        <a
                class="inline-block leading-9 border-2 rounded-full md:px-3 lg:px-6 uppercase"
                class:bg-brand-primary-dark-green={_indicator.route === indicator.route}
                class:text-white={_indicator.route === indicator.route}
                href={`${base}/${lifestage.route}/${_indicator.route}`}
        >{_indicator.name}</a>
    {/each}
</div>
<script>
    import Card from './cards/Card.svelte'
    import {base} from '$app/paths'
    import {lifestages} from "$lib/domain/Lifestage.ts";

    export let lifestage;
</script>

<div class="hidden md:grid col-span-1 row-span-2 text-xl auto-rows-min gap-4">
    <Card>
        <ul class="uppercase font-mono whitespace-nowrap">
            {#each lifestages as _lifestage}
                {#if lifestage === _lifestage}
                    <li class="font-bold leading-8">{_lifestage.name}</li>
                {:else}
                    <li class="indent-2">
                        <a href={`${base}/${_lifestage.route}/access`}>{_lifestage.name}</a>
                    </li>
                {/if}
            {/each}
            {#if !lifestage}
                <li class="font-bold leading-8">scorecard</li>
            {:else}
                <li class="indent-2"><a href={`${base}/scorecard`}>scorecard</a></li>
            {/if}
        </ul>
    </Card>
    <div class="bg-brand-primary-dark-green-banner-background text-white px-6 py-6">
        <h1>Life Stages</h1>
        <div class="py-4 text-base text-light-gray">
            <p>Magnet school enrollment rate relative to population size in...</p>
        </div>
        <div class="text-base text-light-gray">
            <p>Learn more about equity index</p>
        </div>
    </div>
</div>
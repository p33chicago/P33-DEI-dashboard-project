<script type="ts">
    import {slide} from "svelte/transition";
    import Card from "$lib/cards/Card.svelte";
    import Lipsum from '$lib/Lipsum.svelte';
    import { base } from '$app/paths';
    import Access from "$lib/Access.svelte"

    export let data;
</script>

<Card>
    <a href={`${base}/k8${ data.indicator ? '/' : '/access' }`} class="text-dark-gray">
        <div class="grid grid-cols-2">
            <div>
                <h1>Access</h1>
                <p>85.5</p>
            </div>
            <div class="pt-4">
                <p>How much access do black and latino communities have to the resources 
                and opportunities necessary to succeed on a computer science pathway?</p>
            </div>
        </div>
        
        {#if data.indicator === 'access' }
            <!-- <p transition:slide>
                <Lipsum words="30" />
            </p> -->
            <Access />
        {/if}
    </a>
</Card>
<div class="md:invisible">
    <Card>
        <a href={`${base}/k8${ data.indicator ? '/' : '/proficiency' }`} class="text-dark-gray">
            <h1>Proficiency</h1>
            <p>This is the awesome stuff that some poeple have and some people don't</p>
            {#if data.indicator === 'proficiency' }
                <p transition:slide>
                    <Lipsum words="30" />
                </p>
            {/if}
        </a>
    </Card>
</div>
<div class="md:invisible">
    <Card>
        <a href={`${base}/k8${ data.indicator ? '/' : '/excellence' }`} class="text-dark-gray">
            <h1>Excellence</h1>
            <p>This is the awesome stuff that some poeple have and some people don't</p>
            {#if data.indicator === 'excellence' }
                <p transition:slide>
                    <Lipsum words="30" />
                </p>
            {/if}
        </a>
    </Card>
</div>

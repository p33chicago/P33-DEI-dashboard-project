<script type="ts">
    import { slide } from "svelte/transition";
    import Card from "$lib/cards/Card.svelte";
    import Lipsum from '$lib/Lipsum.svelte';

    export let data;
</script>

<a href="/k8{ data.indicator ? '/' : '/access' }">
<Card>
    <h1>Access</h1>
    <p>This is the awesome stuff that some poeple have and some people don't</p>
    {#if data.indicator === 'access' }
        <p transition:slide>
            <Lipsum words="30" />
        </p>
    {/if}
</Card>
</a>

<a href="/k8{ data.indicator ? '/' : '/proficiency' }">
    <div class="lg:invisible">
        <Card>
            <h1>Proficiency</h1>
            <p>This is the awesome stuff that some poeple have and some people don't</p>
            {#if data.indicator === 'proficiency' }
                <p transition:slide>
                    <Lipsum words="30" />
                </p>
            {/if}
        </Card>
    </div>
</a>


<a href="/k8{ data.indicator ? '/' : '/excellence' }">
    <div class="lg:invisible">
        <Card>
            <h1>Excellence</h1>
            <p>This is the awesome stuff that some poeple have and some people don't</p>
            {#if data.indicator === 'excellence' }
                <p transition:slide>
                    <Lipsum words=30 />
                </p>
            {/if}
        </Card>
    </div>
</a>

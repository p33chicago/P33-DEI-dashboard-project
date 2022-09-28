<script type="ts">
    import BodyContentContainer from "$lib/BodyContentContainer.svelte";

    export let title: string;
    export let subtitle: string;
</script>

<div class="font-sans-alternate bg-chicago bg-background-map bg-blend-screen bg-repeat">
    <BodyContentContainer>
        <div class="col-span-4">
            <h1 class="text-white">{title}</h1>
            <h2 class="text-heads-up-yellow">{subtitle}</h2>
        </div>
    </BodyContentContainer>
</div>
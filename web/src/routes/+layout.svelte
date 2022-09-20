<script lang="ts">
    import '../app.css';
    import Header from '$lib/header/Header.svelte';
    import Tota11y from '$lib/Tota11y.svelte';
    import MainContent from "$lib/MainContent.svelte";

    export const csr = false;
    export const prerender = true;
</script>

<svelte:head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fjalla+One&family=Roboto&family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet">
</svelte:head>

<div class="font-sans min-h-full flex flex-col">
    <Header/>
    <MainContent>
        <slot/>
    </MainContent>
    <Tota11y/>
</div>

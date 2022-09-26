<script>
    import SocialButtons from "./SocialButtons.svelte";

    export let header;
    export let subheader;
</script>

<div class="py-6">
    <h2>{header}</h2>
    <p>{subheader}</p>
</div>
<div class="grid grid-cols-2 gap-4">
    <div>
        <h4 class="underline">What does the data tell?</h4>
        <slot name="story"/>

        <h5 class="pt-4 underline">Takeaways</h5>
        <slot name="takeaways"/>
    </div>
    <div class="">
        <slot name="figure"/>
    </div>
</div>
<SocialButtons/>
<hr/>
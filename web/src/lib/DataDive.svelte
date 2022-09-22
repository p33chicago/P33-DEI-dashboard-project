<script>
    import SocialButtons from "./SocialButtons.svelte";
    export let sectionHeader;
    export let sectionSubHeader;
    export let talkingPoint1;
    export let talkingPoint2;
    export let takeaway1;
    export let takeaway2;
</script>

<div class="py-6">
    <h2>{sectionHeader}</h2>
    <p>{sectionSubHeader}</p>
</div>
<div class="grid grid-cols-2 gap-4">
    <div>
        <h4 class="underline">What does the data tell?</h4>
        <p>
            {talkingPoint1}
        </p>
        <p>
            {talkingPoint2}
        </p>

        <h5 class="pt-4 underline">Takeaways</h5>
        <p>
            {takeaway1}
        </p>
        <p>
            {takeaway2}
        </p>
    </div>
    <div class="box-border h-96 w-128 p-4 border-4">GRAPH?</div>
</div>
<SocialButtons />
<hr/>
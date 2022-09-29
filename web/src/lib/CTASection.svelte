<script type="ts">
    export let title: string;
    export let href: string;
    export let link_text: string;
</script>

    <slot name="graphic"/>
    <div class="px-9 py-7">
        <h2 class="text-3xl font-sans-alternate text-black">What can you do to help?</h2>
        <p class="font-mono">Every organization can play a role in building a more inclusive TechChicago</p>
        <a class="inline-block leading-10 bg-brand-primary-dark-green text-white border-2 rounded-full font-sans-alternate mt-3.5 px-11 uppercase"
           {href}>
            {link_text}
        </a>
    </div>
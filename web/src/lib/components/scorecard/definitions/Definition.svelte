<script type="ts">
	import type { Indicator } from '../../../domain/Indicator';
	import { access, excellence, proficiency } from '../../../domain/Indicator';

	export let indicator: Indicator;
</script>

<h3 class="text-white font-sans-alternate text-2xl uppercase">
	<span
		class="rounded-full inline-block w-[25px] h-[25px] align-[-2px] mr-2.5"
		class:bg-blue={indicator === access}
		class:bg-green={indicator === proficiency}
		class:bg-warn-orange={indicator === excellence}
	/>
	{indicator.name}
</h3>
<p>
	<slot />
</p>

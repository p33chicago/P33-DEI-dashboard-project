<script type="ts">
	import Figure from '$lib/components/figure/Figure.svelte';
	import DataDive from '$lib/components/DataDive.svelte';
	import { highSchool } from '$lib/domain/Lifestage';
</script>

<svelte:head>
	<meta content="Help promote equity in tech." name="description" />
</svelte:head>

<DataDive header="AP Computer Science Enrollment" subheader="Percent of CPS HS students enrolled in AP Computer Science">
	<svelte:fragment slot="story">
		<p>
			Asian students have the highest AP CS enrollment rate at 8%, 1.2 times higher than White students, 4
			times higher than Hispanic students, and 7 times higher than Black students.
		</p>
		<p>
			The AP CS enrollment rate for CPS students is significantly higher than the national average across all racial and ethnic groups.
		</p>
	</svelte:fragment>
	<svelte:fragment slot="takeaways">
		<p>
			CPS compares well to national districts in its AP CS enrollment, but has enormous disparities to address.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/apcs_enrol`} slot="figure" />
</DataDive>

<DataDive
	header="CPS HS STEM Magnet School Enrollment"
	subheader="Percent of CPS HS students enrolled in a STEM magnet school by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p>
			Asian students have the highest AP CS enrollment rate of 8%. 1.2 times higher than White, 4
			times higher than Hispanics, and 7 times higher than black.
		</p>
	</svelte:fragment>
	<svelte:fragment slot="takeaways">
		<p>
			13.25% of Black students enrolled in STEM Magnet elementary schools while only 8.82% enrolled
			in STEM Magnet high school.
		</p>
		<p>
			7.87% of Hispanic students enrolled in STEM Magnet elementary schools while 19.66% enrolled in
			STEM Magnet high school.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/magnet_enrol`} slot="figure" />
</DataDive>

<DataDive
	header="CS Interest"
	subheader="Percent of CPS HS students indicating interest in an CS/IT career"
>
	<svelte:fragment slot="takeaways">
		<p>
			1 out of 4 Asian students express an interest in Computer Science, in comparison with 1 out of
			5 white students, 1 out of 10 Hispanic students, and 1 out of 20 black students expressing the
			same interest.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/CSInterested`} slot="figure" />
</DataDive>

<DataDive
	header="Advanced Math Enrollment"
	subheader="Percent of CPS SAT takers exceeding standards by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p>
			In Chicago, almost 4 out of 10 White and Asian students in CPS enrolled in advanced math
			class, 3 out of 10 Black and Hispanic students enrolled in advanced math class.
		</p>
		<p>
			Overall, the proportion of students who enrolled in advanced math classes in CPS is twice the
			proportion in the national average.
		</p>
	</svelte:fragment>

	<svelte:fragment slot="takeaways">
		<p>
			Minor racial disparity detected in advanced math enrollment rate. Superior performances of CPS
			in related to the national average.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/advMath_enrol`} slot="figure" />
</DataDive>

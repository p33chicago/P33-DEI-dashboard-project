import type {Load} from "@sveltejs/kit";
import type {Scorecard} from "$lib/domain/scorecard.ts";
import {scorecard} from "$lib/domain/scorecard.ts";

export const load: Load<{ scorecard: Scorecard }> = async () => {
    return {scorecard}
}
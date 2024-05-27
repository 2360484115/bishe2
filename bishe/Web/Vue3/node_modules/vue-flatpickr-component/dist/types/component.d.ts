import flatpickr from 'flatpickr';
import type { PropType } from 'vue';
declare const _default: import("vue").DefineComponent<{
    modelValue: {
        type: PropType<import("flatpickr/dist/types/options").DateOption | import("flatpickr/dist/types/options").DateOption[] | null>;
        required: true;
    };
    config: {
        type: PropType<Partial<import("flatpickr/dist/types/options").BaseOptions>>;
        default: () => {
            defaultDate: null;
            wrap: boolean;
        };
    };
    events: {
        type: PropType<import("flatpickr/dist/types/options").HookKey[]>;
        default: () => import("flatpickr/dist/types/options").HookKey[];
    };
    disabled: {
        type: BooleanConstructor;
        default: boolean;
    };
}, unknown, {
    fp: import("flatpickr/dist/types/instance").Instance | null;
}, {}, {
    prepareConfig(): flatpickr.Options.Options;
    /**
     * Get the HTML node where flatpickr to be attached
     * Bind on parent element if wrap is true
     */
    getElem(): HTMLInputElement;
    /**
     * Watch for value changed by date-picker itself and notify parent component
     */
    onInput(event: InputEvent): void;
    fpInput(): HTMLInputElement;
    /**
     * Blur event is required by many validation libraries
     */
    onBlur(event: Event): void;
    /**
     * Flatpickr does not emit input event in some cases
     */
    onClose(selectedDates: Date[], dateStr: string): void;
    /**
     * Watch for the disabled property and sets the value to the real input.
     */
    watchDisabled(newState: boolean): void;
}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, ("blur" | "update:modelValue" | "on-change" | "on-close" | "on-day-create" | "on-destroy" | "on-key-down" | "on-month-change" | "on-open" | "on-parse-config" | "on-ready" | "on-value-update" | "on-year-change" | "on-pre-calendar-position")[], "blur" | "update:modelValue" | "on-change" | "on-close" | "on-day-create" | "on-destroy" | "on-key-down" | "on-month-change" | "on-open" | "on-parse-config" | "on-ready" | "on-value-update" | "on-year-change" | "on-pre-calendar-position", import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    modelValue: {
        type: PropType<import("flatpickr/dist/types/options").DateOption | import("flatpickr/dist/types/options").DateOption[] | null>;
        required: true;
    };
    config: {
        type: PropType<Partial<import("flatpickr/dist/types/options").BaseOptions>>;
        default: () => {
            defaultDate: null;
            wrap: boolean;
        };
    };
    events: {
        type: PropType<import("flatpickr/dist/types/options").HookKey[]>;
        default: () => import("flatpickr/dist/types/options").HookKey[];
    };
    disabled: {
        type: BooleanConstructor;
        default: boolean;
    };
}>> & {
    onBlur?: ((...args: any[]) => any) | undefined;
    "onUpdate:modelValue"?: ((...args: any[]) => any) | undefined;
    "onOn-change"?: ((...args: any[]) => any) | undefined;
    "onOn-close"?: ((...args: any[]) => any) | undefined;
    "onOn-day-create"?: ((...args: any[]) => any) | undefined;
    "onOn-destroy"?: ((...args: any[]) => any) | undefined;
    "onOn-key-down"?: ((...args: any[]) => any) | undefined;
    "onOn-month-change"?: ((...args: any[]) => any) | undefined;
    "onOn-open"?: ((...args: any[]) => any) | undefined;
    "onOn-parse-config"?: ((...args: any[]) => any) | undefined;
    "onOn-ready"?: ((...args: any[]) => any) | undefined;
    "onOn-value-update"?: ((...args: any[]) => any) | undefined;
    "onOn-year-change"?: ((...args: any[]) => any) | undefined;
    "onOn-pre-calendar-position"?: ((...args: any[]) => any) | undefined;
}, {
    config: Partial<import("flatpickr/dist/types/options").BaseOptions>;
    events: import("flatpickr/dist/types/options").HookKey[];
    disabled: boolean;
}, {}>;
export default _default;

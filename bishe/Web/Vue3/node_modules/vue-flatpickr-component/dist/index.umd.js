(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory(require("flatpickr"), require("vue"));
	else if(typeof define === 'function' && define.amd)
		define("VueFlatpickr", ["flatpickr", "vue"], factory);
	else if(typeof exports === 'object')
		exports["VueFlatpickr"] = factory(require("flatpickr"), require("vue"));
	else
		root["VueFlatpickr"] = factory(root["flatpickr"], root["Vue"]);
})(this, (__WEBPACK_EXTERNAL_MODULE__311__, __WEBPACK_EXTERNAL_MODULE__976__) => {
return /******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 311:
/***/ ((module) => {

module.exports = __WEBPACK_EXTERNAL_MODULE__311__;

/***/ }),

/***/ 976:
/***/ ((module) => {

module.exports = __WEBPACK_EXTERNAL_MODULE__976__;

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
(() => {
// ESM COMPAT FLAG
__webpack_require__.r(__webpack_exports__);

// EXPORTS
__webpack_require__.d(__webpack_exports__, {
  "default": () => (/* binding */ src)
});

// EXTERNAL MODULE: external "flatpickr"
var external_flatpickr_ = __webpack_require__(311);
var external_flatpickr_default = /*#__PURE__*/__webpack_require__.n(external_flatpickr_);
// EXTERNAL MODULE: external {"commonjs":"vue","commonjs2":"vue","amd":"vue","root":"Vue"}
var external_commonjs_vue_commonjs2_vue_amd_vue_root_Vue_ = __webpack_require__(976);
;// CONCATENATED MODULE: ./src/events.ts
const includedEvents = [
    'onChange',
    'onClose',
    'onDestroy',
    'onMonthChange',
    'onOpen',
    'onYearChange',
];
// Let's not emit these events by default
const excludedEvents = [
    'onValueUpdate',
    'onDayCreate',
    'onParseConfig',
    'onReady',
    'onPreCalendarPosition',
    'onKeyDown',
];


;// CONCATENATED MODULE: ./src/util.ts
function camelToKebab(string) {
    return string.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
}
function arrayify(obj) {
    return obj instanceof Array
        ? obj
        : [obj];
}
function nullify(value) {
    return (value && value.length)
        ? value
        : null;
}


;// CONCATENATED MODULE: ./src/component.ts




// Keep a copy of all events for later use
const allEvents = [...includedEvents, ...excludedEvents];
// Passing these properties in `fp.set()` method will cause flatpickr to trigger some callbacks
const configCallbacks = ['locale', 'showMonths'];
/* harmony default export */ const component = ((0,external_commonjs_vue_commonjs2_vue_amd_vue_root_Vue_.defineComponent)({
    name: 'FlatPickr',
    compatConfig: {
        MODE: 3,
    },
    render() {
        return (0,external_commonjs_vue_commonjs2_vue_amd_vue_root_Vue_.h)('input', {
            type: 'text',
            'data-input': true,
            disabled: this.disabled,
            onInput: this.onInput,
        });
    },
    emits: [
        'blur',
        'update:modelValue',
        ...allEvents.map(camelToKebab)
    ],
    props: {
        modelValue: {
            type: [String, Number, Date, Array, null],
            required: true,
        },
        // https://flatpickr.js.org/options/
        config: {
            type: Object,
            default: () => ({
                defaultDate: null,
                wrap: false,
            })
        },
        events: {
            type: Array,
            default: () => includedEvents
        },
        disabled: {
            type: Boolean,
            default: false
        },
    },
    data() {
        return {
            fp: null, //todo make it non-reactive
        };
    },
    mounted() {
        // Return early if flatpickr is already loaded
        /* istanbul ignore if */
        if (this.fp)
            return;
        // Init flatpickr
        this.fp = external_flatpickr_default()(this.getElem(), this.prepareConfig());
        // Attach blur event
        this.fpInput().addEventListener('blur', this.onBlur);
        // Immediate watch will fail before fp is set,
        // so we need to start watching after mount
        this.$watch('disabled', this.watchDisabled, {
            immediate: true
        });
    },
    methods: {
        prepareConfig() {
            // Don't mutate original object on parent component
            let safeConfig = Object.assign({}, this.config);
            this.events.forEach((hook) => {
                // Respect global callbacks registered via setDefault() method
                let globalCallbacks = (external_flatpickr_default()).defaultConfig[hook] || [];
                // Inject our own method along with user's callbacks
                let localCallback = (...args) => {
                    this.$emit(camelToKebab(hook), ...args);
                };
                // Overwrite with merged array
                safeConfig[hook] = arrayify(safeConfig[hook] || []).concat(globalCallbacks, localCallback);
            });
            const onCloseCb = this.onClose.bind(this);
            safeConfig['onClose'] = arrayify(safeConfig['onClose'] || []).concat(onCloseCb);
            // Set initial date without emitting any event
            safeConfig.defaultDate = this.modelValue || safeConfig.defaultDate;
            return safeConfig;
        },
        /**
         * Get the HTML node where flatpickr to be attached
         * Bind on parent element if wrap is true
         */
        getElem() {
            return this.config.wrap ? this.$el.parentNode : this.$el;
        },
        /**
         * Watch for value changed by date-picker itself and notify parent component
         */
        onInput(event) {
            const input = event.target;
            // Let's wait for DOM to be updated
            (0,external_commonjs_vue_commonjs2_vue_amd_vue_root_Vue_.nextTick)().then(() => {
                this.$emit('update:modelValue', nullify(input.value));
            });
        },
        fpInput() {
            return this.fp.altInput || this.fp.input;
        },
        /**
         * Blur event is required by many validation libraries
         */
        onBlur(event) {
            this.$emit('blur', nullify(event.target.value));
        },
        /**
         * Flatpickr does not emit input event in some cases
         */
        onClose(selectedDates, dateStr) {
            this.$emit('update:modelValue', dateStr);
        },
        /**
         * Watch for the disabled property and sets the value to the real input.
         */
        watchDisabled(newState) {
            if (newState) {
                this.fpInput().setAttribute('disabled', '');
            }
            else {
                this.fpInput().removeAttribute('disabled');
            }
        }
    },
    watch: {
        /**
         * Watch for any config changes and redraw date-picker
         */
        config: {
            deep: true,
            handler(newConfig) {
                if (!this.fp)
                    return;
                let safeConfig = Object.assign({}, newConfig);
                // Workaround: Don't pass hooks to configs again otherwise
                // previously registered hooks will stop working
                // Notice: we are looping through all events
                // This also means that new callbacks can not be passed once component has been initialized
                allEvents.forEach((hook) => {
                    delete safeConfig[hook];
                });
                this.fp.set(safeConfig);
                // Workaround: Allow to change locale dynamically
                configCallbacks.forEach((name) => {
                    if (typeof safeConfig[name] !== 'undefined') {
                        this.fp.set(name, safeConfig[name]);
                    }
                });
            }
        },
        /**
         * Watch for changes from parent component and update DOM
         */
        modelValue(newValue) {
            var _a;
            // Prevent updates if v-model value is same as input's current value
            if (!this.$el || newValue === nullify(this.$el.value))
                return;
            // Notify flatpickr instance that there is a change in value
            (_a = this.fp) === null || _a === void 0 ? void 0 : _a.setDate(newValue, true);
        }
    },
    beforeUnmount() {
        /* istanbul ignore else */
        if (!this.fp)
            return;
        this.fpInput().removeEventListener('blur', this.onBlur);
        this.fp.destroy();
        this.fp = null;
    }
}));

;// CONCATENATED MODULE: ./src/index.ts

/* harmony default export */ const src = (component);

})();

/******/ 	return __webpack_exports__;
/******/ })()
;
});
import { defineStore } from 'pinia';
import { i18n } from '../i18n';


export const sharedStore = defineStore('shared-vue', {
    state: () => ({
        sizePerPage: 50,
    }),
    getters: {},
    actions: {
        $t(key) {
            return i18n.t(key);
        },
        error(code = 400, message = '') {
            this.$router.replace({ name: 'error', state: { code: code, message: message } });
        },
        replace(name, params = {}, query = {}) {
            this.$router.replace({ name: name, params: params, query: query });
        },
        push(name, params = {}, query = {}) {
            this.$router.push({ name: name, params: params, query: query });
        },
    },
});
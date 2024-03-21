import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: '',
  },
  getters: {
    getUserId: (state) => state.userId,
  },
  mutations: {
    setUserId(state, id) {
      state.userId = id;
    },
  },
  actions: {
    setUserId({ commit }, value) {
      commit('setUserId', value);
    },
  },
  modules: {
  },
});

<template>
  <v-container
    fluid
    fill-height
  >
    <v-snackbar
      v-model="alert"
      :color="alertColor"
    >
      {{ alertMessage }}
    </v-snackbar>
    <div class="bg-image" />
    <v-row>
      <v-col align="center">
        <v-card
          elevation="6"
          width="40%"
        >
          <v-row>
            <v-col>
              <v-img
                src="../assets/alifex_logo.png"
                alt="alifex logo"
                max-height="150"
                max-width="150"
                class="mt-4"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-form
                ref="form"
                v-model="isFormValid"
                class="mt-5 mb-5"
              >
                <v-row
                  justify="center"
                  no-gutters
                >
                  <v-col
                    cols="8"
                  >
                    <v-text-field
                      id="email-field"
                      v-model="formData.email"
                      :rules="emailRules"
                      label="Email address"
                      outlined
                      prepend-inner-icon="mdi-email"
                    />
                  </v-col>
                </v-row>
                <v-row
                  justify="center"
                  no-gutters
                >
                  <v-col
                    cols="8"
                  >
                    <v-text-field
                      id="password-field"
                      v-model="formData.password"
                      :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="passwordRules"
                      :type="value ? 'password' : 'text'"
                      label="Password"
                      outlined
                      prepend-inner-icon="mdi-lock"
                      @click:append="() => (value = !value)"
                    />
                  </v-col>
                </v-row>
                <v-row
                  no-gutters
                >
                  <v-col>
                    <v-btn
                      id="login-btn"
                      :disabled="!isFormValid"
                      width="67%"
                      @click="loginAccount"
                    >
                      Login
                    </v-btn>
                  </v-col>
                </v-row>
                <v-row
                  justify="center"
                >
                  <v-col cols="8">
                    <p>Don't have an account? Create one for free
                    <a :href="registerLink">here</a></p>
                  </v-col>
                </v-row>
              </v-form>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// External
import { mapActions } from 'vuex';

// Internal
import API from '../api/methods';

export default {
  name: 'LoginView',
  data() {
    return {
      alert: false,
      alertColor: '',
      alertMessage: '',
      isFormValid: false,
      value: String,
      formData: {
        email: '',
        password: '',
      },
      emailRules: [
        (v) => !!v || 'E-mail is required',
        (v) => /^([a-zA-Z0-9_\-.]+)@([a-zA-Z0-9_\-.]+)\.([a-zA-Z]{2,5})$/.test(v) || 'Not a valid e-mail address',
      ],
      passwordRules: [
        (v) => !!v || 'Password is required',
        (v) => v.length >= 6 || 'Password should be at least 6 characters',
        (v) => v.length <= 24 || 'Maximum password length is 24 characters',
        (v) => /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/.test(v) || 'Password must contain an uppercase, number and special charater',
      ],
      registerLink: '/register',
    };
  },
  methods: {
    ...mapActions(['setUserId']),
    async loginAccount() {
      if (this.$refs.form.validate()) {
        const DATA = {
          email: this.formData.email,
          password: this.formData.password,
        };
        const RESPONSE = await API.loginUser(DATA);
        if (RESPONSE.data.success === true) {
          this.setUserId(RESPONSE.data.data.user_id);
          setTimeout(() => this.$router.push({ path: '/home' }));
        } else {
          this.alertMessage = RESPONSE.data.message;
          this.alertColor = 'red';
          this.alert = true;
        }
      }
    },
  },
};
</script>

<style scoped>
.bg-image {
  background-image: url(../assets/bg.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  opacity: 0.08;
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100vw;
}
</style>

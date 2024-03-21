<template>
  <v-container
    fluid
    fill-height
  >
    <div class="bg-image" />
    <v-snackbar
      v-model="alert"
      :color="alertColour"
    >
      {{ alertMessage }}
    </v-snackbar>
    <v-row>
      <v-col align="center">
        <v-card
          elevation="6"
          width="40%"
        >
          <v-row>
            <v-col>
              <h1 class="mb-2 mt-2">
                Create an account
              </h1>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-form
                ref="form"
                class="mb-5"
              >
                <v-row
                  justify="center"
                  no-gutters
                >
                  <v-col cols="8">
                    <v-text-field
                      v-model="email"
                      label="Email address"
                      outlined
                      prepend-inner-icon="mdi-email"
                      :rules="emailRules"
                    />
                  </v-col>
                </v-row>
                <v-row
                  justify="center"
                  no-gutters
                >
                  <v-col cols="8">
                    <v-text-field
                      v-model="username"
                      label="Username"
                      outlined
                      prepend-inner-icon="mdi-account"
                      :rules="usernameRules"
                    />
                  </v-col>
                </v-row>
                <v-row
                  justify="center"
                  no-gutters
                >
                  <v-col cols="8">
                    <v-text-field
                      v-model="password"
                      label="Password"
                      outlined
                      type="password"
                      prepend-inner-icon="mdi-lock"
                      :rules="passwordRules"
                    />
                  </v-col>
                </v-row>
                <v-row
                  justify="center"
                  no-gutters
                >
                  <v-col cols="8">
                    <v-text-field
                      v-model="passwordConfirmation"
                      label="Re-enter password"
                      outlined
                      type="password"
                      prepend-inner-icon="mdi-lock"
                      :rules="passwordConfirmationRules"
                    />
                  </v-col>
                </v-row>
                <v-row
                  justify="center"
                  no-gutters
                >
                </v-row>
                <v-row
                  no-gutters
                >
                  <v-col>
                    <v-btn
                      width="67%"
                      @click="registerAccount"
                    >
                      Create account
                    </v-btn>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <p>Already have an account? Login <a :href="loginLink">here</a></p>
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
import API from '../api/methods';

export default {
  data() {
    return {
      alert: false,
      alertColour: '',
      alertMessage: '',
      email: '',
      username: '',
      password: '',
      passwordConfirmation: '',
      emailRules: [
        (v) => !!v || 'E-mail is required',
        (v) => /^([a-zA-Z0-9_\-.]+)@([a-zA-Z0-9_\-.]+)\.([a-zA-Z]{2,5})$/.test(v) || 'Not a valid e-mail address',
      ],
      usernameRules: [
        (v) => !!v || 'Username is required',
        (v) => v.length >= 6 || 'Username should be atleast 6 characters',
        (v) => v.length <= 15 || 'Maximum username length is 15 characters',
      ],
      passwordRules: [
        (v) => !!v || 'Password is required',
        (v) => v.length >= 6 || 'Password should be atleast 6 characters',
        (v) => v.length <= 24 || 'Maximum password length is 24 characters',
        (v) => /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$/.test(v) || 'Password must contain an uppercase, number and special charater',
      ],
      passwordConfirmationRules: [
        (v) => !!v || 'Password confirmation is required',
        () => this.password === this.passwordConfirmation || "The re-entered password doesn't match",
      ],
      termsOfServiceRules: [(v) => !!v],
      loginLink: '/login',
    };
  },
  methods: {
    /**
     * Reigsters a new account by sending POST request to user api.
     */
    async registerAccount() {
      if (this.$refs.form.validate()) {
        const DATA = {
          email: this.email.toLowerCase(),
          username: this.username.toLowerCase(),
          password: this.password,
        };
        const RESPONSE = await API.createAccount(DATA);
        if (RESPONSE.data.success === true) {
          this.alertMessage = RESPONSE.data.message;
          this.alertColour = 'success';
          this.alert = true;
          setTimeout(() => this.$router.push({ path: '/login' }), 1500);
        } else {
          this.alertMessage = RESPONSE.data.error;
          this.alertColour = 'red';
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

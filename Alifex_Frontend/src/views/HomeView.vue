<template>
  <v-container fluid fill-height style="height: 10px;">
    <v-snackbar v-model="alert" :color="alertColor">
      {{ alertMessage }}
    </v-snackbar>
    <v-row style="height: 700px">
      <v-col cols="10">
        <v-container
          class="grid-container"
          :style="{ 'backgroundImage': 'url(' + backgroundImage + ')' }"
          fluid
          v-if="containerVisible"
        >
          <v-row>
            <v-col
              v-for="(row, rowIndex) in gridLayout"
              :key="rowIndex"
              cols="10"
              :class="['d-flex', 'no-margin', { 'first-row-padding': rowIndex === 0 }]"
            >
              <v-row
                v-for="(col, colIndex) in row"
                :key="colIndex"
                :style="{ height: rowHeight + 'px' }"
                :class="['no-margin', { 'first-col-padding': colIndex === 0 }]"
              >
                <v-col :cols="10 / 5" class="grid-cell">
                  <v-btn
                    v-if="col !== null"
                    @click="showFishDetails(col)"
                    icon
                    class="d-flex justify-center align-center"
                  >
                    <v-img
                      :src="getFishImage(col)"
                      alt="Fish Image"
                      width="50"
                      height="50"
                    />
                  </v-btn>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-container>
      </v-col>
      <v-col
        cols="2"
        style="background-color: #002159; position: relative; height: 716px"
      >
        <v-row class="text-center">
          <v-col
            class="d-flex justify-center align-center"
          >
            <v-img
              src="../assets/alifex_logo.png"
              alt="alifex logo"
              max-height="150"
              max-width="150"
              class="mt-4"
            />
          </v-col>
        </v-row>
        <v-row dense>
          <v-col class="d-flex justify-center align-center">
            <span class="white--text text-h6" >
              Ku {{ this.kudos }}
            </span>
          </v-col>
        </v-row>
        <v-row dense>
          <v-col class="d-flex justify-center align-center">
            <span class="white--text text-h6" >
              {{ this.fishNumber }}
            </span>
          </v-col>
        </v-row>
        <v-row dense>
          <v-col class="d-flex justify-center align-center">
           <span class="white--text text-h6" >
             Age {{ this.userAge }}
          </span>
          </v-col>
        </v-row>
        <v-row class="py-5">
          <v-col class="d-flex justify-center align-center pa-5">
            <v-btn icon @click="showTankDialog">
              <img
                src="../assets/tankdetails.png"
                alt="Tank Details"
                width="100"
                height="100"
              >
            </v-btn>
          </v-col>
          <v-col class="d-flex justify-center align-center pa-5">
            <v-btn icon @click="advanceDay">
              <img
                src="../assets/newday.png"
                alt="New Day"
                width="100"
                height="100"
              >
            </v-btn>
          </v-col>
        </v-row>
        <v-row class="py-5">
          <v-col class="d-flex justify-center align-center pa-5">
            <v-btn icon @click="showBibleGroup">
              <img
                src="../assets/breederbible.png"
                alt="Breeder Bible"
                width="100"
                height="100"
              >
            </v-btn>
          </v-col>
          <v-col class="d-flex justify-center align-center pa-5">
            <v-btn icon @click="showBuy">
              <img
                src="../assets/buyfish.png"
                alt="Buy Fish"
                width="100"
                height="100"
              >
            </v-btn>
          </v-col>
        </v-row>
        <v-row class="py-5">
          <v-col class="d-flex justify-center align-center pa-5">
            <v-btn icon @click="showTank">
              <img
                src="../assets/tank.png"
                alt="Tank"
                width="100"
                height="100"
              >
            </v-btn>
          </v-col>
          <v-col class="d-flex justify-center align-center pa-5">
            <v-btn icon @click="showFrozenTank">
              <img
                src="../assets/freezer.png"
                alt="Freezer"
                width="100"
                height="100"
              >
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-dialog
      v-model="fishDialog"
      width="500px"
    >
      <v-card style="background-color: #99d9ea;">
        <div class="d-flex">
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h6 text-right pt-8"
            style="color: #8B0000;"
          >
            {{ selectedFish[currentFishIndex][4] }} {{ selectedFish[currentFishIndex][2] }}
          </v-card-text>
          <v-card-text class="d-flex justify-left align-left pt-3 pb-0">
            <v-img
              v-if="selectedFish[currentFishIndex]"
              :src="getFishImage(selectedFish[currentFishIndex][2])"
              alt="Fish Image"
              max-width="75"
              max-height="75"
            />
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h6 text-center"
            style="color: #8B0000;"
          >
            Age:
          </v-card-text>
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h6 text-left"
            style="color: #8B0000;"
          >
            {{ selectedFish[currentFishIndex][5] }} days
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h6 text-center"
            style="color: #8B0000;"
          >
            Weight:
          </v-card-text>
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h6 text-left"
            style="color: #8B0000;"
          >
            {{ Math.floor(selectedFish[currentFishIndex][7]) }}g
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h6 text-center"
            style="color: #8B0000;"
          >
            Worth:
          </v-card-text>
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h6 text-left"
            style="color: #8B0000;"
          >
            Ku{{ Math.floor(selectedFish[currentFishIndex][8]) }}
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-actions class="d-flex justify-space-between">
            <v-btn
              class="text-left pl-8"
              @click=openSellFishDialog()
              icon
            >
              <img
                src="../assets/sellfish.png"
                alt="Sell Fish"
                width="50"
                height="50"
              />
            </v-btn>
            <v-btn
              class="mx-auto"
              icon
              @click="changeFrozenStatus"
            >
              <img
                src="../assets/freezer.png"
                alt="Freezer"
                width="50"
                height="50"
              />
            </v-btn>
            <v-btn
              class="text-right pr-8"
              icon
              @click="openBibleDialog(selectedFish[currentFishIndex][2])"
            >
              <img
                src="../assets/breederbible.png"
                alt="Breeders Bible"
                width="50"
                height="50"
              />
            </v-btn>
          </v-card-actions>
        </div>
        <div class="pa-5">
          <v-card-actions class="d-flex justify-between">
            <v-btn
              color="primary"
              @click="showPreviousFish"
              :disabled="!hasPreviousFish"
            >
              Previous Fish
            </v-btn>
            <v-btn
              color="primary"
              @click="closeFishDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
            <v-btn
              color="primary"
              @click="showNextFish"
              :disabled="!hasNextFish"
              class="ml-auto"
            >
              Next Fish
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog
      v-model="sellFishDialog"
      width="500px"
    >
      <v-card style="background-color: #99d9ea;">
        <div class="d-flex">
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h6 text-right pt-8"
            style="color: #8B0000;"
          >
            {{ selectedFish[currentFishIndex][4] }} {{ selectedFish[currentFishIndex][2] }}
          </v-card-text>
          <v-card-text class="d-flex justify-left align-left pt-3 pb-0">
            <v-img
              v-if="selectedFish[currentFishIndex]"
              :src="getFishImage(selectedFish[currentFishIndex][2])"
              alt="Fish Image"
              max-width="75"
              max-height="75"
            />
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h7 text-centre pt-8"
            style="color: #8B0000;"
          >
            The value of these fish are
            <b>Ku{{ Math.floor(selectedFish[currentFishIndex][8]) }}</b> each
          </v-card-text>
        </div>
        <div class="pa-5 d-flex align-center">
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h7"
            style="color: #8B0000; width: auto;"
          >
            Number to sell:
          </v-card-text>
          <v-text-field
            v-model="sellFishQuantity"
            id="quantity"
            label="Quantity"
            outlined
            :rules="sellFishRules"
            class="ml-3"
          />
        </div>
        <div class="pa-5 d-flex align-center">
          <v-card-text
            v-if="selectedFish[currentFishIndex]"
            class="text-h5"
            style="color: #8B0000; width: auto;"
          >
            Total Ku: {{ sellFishWorth() }}
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-actions class="d-flex justify-between">
            <v-btn
              color="primary"
              class="mx-auto"
              @click="sellFish(selectedFish[currentFishIndex][9])"
            >
              Sell
            </v-btn>
            <v-btn
              color="primary"
              @click="closeSellFishDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog v-model="logDialog" width="500px">
      <v-card style="background-color: #99d9ea;">
        <v-card-text
          class="text-h6 pt-6"
          style="color: #8B0000; width: auto; white-space: pre-line;"
        >
          {{ getCurrentLog() }}
        </v-card-text>
        <v-card-actions>
          <v-btn @click="previousStep" v-if="currentStep > 0" color="primary">Previous</v-btn>
          <v-spacer></v-spacer>
          <v-btn @click="nextStep" v-if="currentStep < 2" color="primary">Next</v-btn>
          <v-btn @click="closeLogDialog" v-if="currentStep == 2" color="primary">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="tankDialog" width="500px">
      <v-card style="background-color: #D3D3D3">
        <div class="pa-5 d-flex justify-between">
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            Day:
          </v-card-text>
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            {{ userAge }}
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            Fish:
          </v-card-text>
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            {{ fishNumber }}
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            Schools:
          </v-card-text>
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            {{ calculateSchools() }}
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            Cash:
          </v-card-text>
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            Ku{{ kudos }}
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            Value:
          </v-card-text>
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            Ku{{ calculateValue() }}
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-actions>
            <v-btn
              color="primary"
              @click="closeTankDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog v-model="freezeDialog" width="500px">
      <v-card style="background-color: #99d9ea">
        <div class="pa-5 d-flex justify-between">
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            How many fish would you like to freeze?:
          </v-card-text>
          <v-text-field
            v-model="freezeFishQuantity"
            id="freezeQuantity"
            label="Quantity"
            outlined
            :rules="freezeFishRules"
            class="ml-3 pt-6"
          />
        </div>
        <div class="pa-5">
          <v-card-actions>
            <v-btn
              color="primary"
              @click="freezeFish()"
              class="mx-auto"
            >
              Freeze
            </v-btn>
            <v-btn
              color="primary"
              @click="closeFreezeDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog v-model="unfreezeDialog" width="500px">
      <v-card style="background-color: #99d9ea">
        <div class="pa-5 d-flex justify-between">
          <v-card-text
            class="black-text text-h6 pt-6"
          >
            How many fish would you like to defrost?:
          </v-card-text>
          <v-text-field
            v-model="unfreezeFishQuantity"
            id="freezeQuantity"
            label="Quantity"
            outlined
            :rules="unfreezeFishRules"
            class="ml-3 pt-6"
          />
        </div>
        <div class="pa-5">
          <v-card-actions>
            <v-btn
              color="primary"
              @click="unfreezeFish()"
              class="mx-auto"
            >
              Defrost
            </v-btn>
            <v-btn
              color="primary"
              @click="closeUnfreezeDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog v-model="buyFishTypesDialog" width="500px">
      <v-card style="background-color: #99d9ea">
        <div>
          <v-card-text
            class="d-flex text-center text-h6 flex-column pt-8"
            style="color: #8B0000;"
          >
            Shop
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
            class="d-flex text-h7 flex-column pt-8"
            style="color: #8B0000;"
          >
            <v-btn icon @click="openFishDialog('Angelfish')">
              <v-img
                src="../assets/Fish/BlazingAngelFish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Angelfish </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openFishDialog('Angle Fish')">
              <v-img
                src="../assets/Fish/AcuteAngleFish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Angle Fish </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openFishDialog('Bass')">
              <v-img
                src="../assets/Fish/DoubleBass.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Bass </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openFishDialog('Catfish')">
              <v-img
                src="../assets/Fish/ManxCatfish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Catfish </span>
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openFishDialog('Choirfish')">
              <v-img
                src="../assets/Fish/YodellingChoirfish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Choirfish </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon @click="openFishDialog('Eel')">
              <v-img
                src="../assets/Fish/AtomicEel.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Eel </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openFishDialog('Europan Shark')">
              <v-img
                src="../assets/Fish/PanShark.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Europan Shark </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openFishDialog('Grouper')">
              <v-img
                src="../assets/Fish/FadedGrouper.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Grouper </span>
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openFishDialog('Philosofish')">
              <v-img
                src="../assets/Fish/NietzschesPhilosofish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Philosofish </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openFishDialog('Piranha')">
              <v-img
                src="../assets/Fish/IonicPiranha.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Piranha </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openFishDialog('Sprat')">
              <v-img
                src="../assets/Fish/WhiteSprat.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Sprat </span>
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-actions>
            <v-btn
              color="primary"
              @click="closeBuyFishTypesDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog v-model="buyFishCategoryDialog" width="500px">
      <v-card style="background-color: #99d9ea">
        <v-row v-for="(fish, index) in fishArray" :key="index" align="center">
          <v-col cols="4">
            <v-card-text
              class="text-h7 text-left pl-8 flex-grow-1"
              style="color: #8B0000;"
            >
              {{ fish.name }}
            </v-card-text>
          </v-col>
          <v-col cols="4">
            <v-card-text
              class="text-h7 mx-auto"
              style="color: #8B0000;"
            >
              Ku{{ fish.buyPrice }}
            </v-card-text>
          </v-col>
          <v-col cols="4">
            <v-card-actions class="pt-5">
              <v-btn icon  @click="openBuySpecificFishDialog(fish.name, fish.buyPrice)">
                <v-img
                  :src="getFishImage(fish.name)"
                  alt="Fish Image"
                  max-width="50"
                  max-height="50"
                />
              </v-btn>
            </v-card-actions>
          </v-col>
        </v-row>
        <div class="pa-5">
          <v-card-actions>
            <v-btn
              color="primary"
              @click="closeBuyFishCategoryDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog v-model="buySpecificFishDialog" width="500px">
      <v-card style="background-color: #99d9ea">
        <div class="d-flex">
          <v-card-text
            class="text-h6 text-right pt-8"
            style="color: #8B0000;"
          >
            {{ this.buyFish[0] }}
          </v-card-text>
          <v-card-text class="d-flex justify-left align-left pt-3 pb-0">
            <v-img
              :src="getFishImage(this.buyFish[0])"
              alt="Fish Image"
              max-width="75"
              max-height="75"
            />
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-text
            class="text-h7 text-centre pt-8"
            style="color: #8B0000;"
          >
            The current Alien Fish Exchange price is <b>Ku{{ this.buyFish[1] }}</b> each
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-text
            class="text-h7 text-right pt-8"
            style="color: #8B0000;"
          >
            You can afford <b>{{ affordFishQuantity() }}</b> fish
          </v-card-text>
        </div>
        <div class="pa-5 d-flex align-center">
          <v-card-text
            class="text-h7"
            style="color: #8B0000; width: auto;"
          >
            Number to buy:
          </v-card-text>
          <v-text-field
            v-model="buyFishQuantity"
            id="buyQuantity"
            label="Quantity"
            outlined
            :rules="buyFishRules"
            class="ml-3"
          />
        </div>
        <div class="pa-5 d-flex align-center">
          <v-card-text
            class="text-h5"
            style="color: #8B0000; width: auto;"
          >
            Total Ku: {{ buyFishWorth() }}
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-actions class="d-flex justify-between">
            <v-btn
              color="primary"
              class="mx-auto"
              @click="buyFishShop()"
            >
              Buy
            </v-btn>
            <v-btn
              color="primary"
              @click="closeBuyFishDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog v-model="bibleGroupDialog" width="500px">
      <v-card style="background-color: #99d9ea">
        <div>
          <v-card-text
            class="d-flex text-center text-h6 flex-column pt-8"
            style="color: #8B0000;"
          >
            Breeder's Bible
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
            class="d-flex text-h7 flex-column pt-8"
            style="color: #8B0000;"
          >
            <v-btn icon @click="openBibleFishDialog('Angelfish')">
              <v-img
                src="../assets/Fish/BlazingAngelFish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Angelfish </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openBibleFishDialog('Angle Fish')">
              <v-img
                src="../assets/Fish/AcuteAngleFish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Angle Fish </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openBibleFishDialog('Bass')">
              <v-img
                src="../assets/Fish/DoubleBass.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Bass </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openBibleFishDialog('Catfish')">
              <v-img
                src="../assets/Fish/ManxCatfish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Catfish </span>
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openBibleFishDialog('Choirfish')">
              <v-img
                src="../assets/Fish/YodellingChoirfish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Choirfish </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon @click="openBibleFishDialog('Eel')">
              <v-img
                src="../assets/Fish/AtomicEel.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Eel </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openBibleFishDialog('Europan Shark')">
              <v-img
                src="../assets/Fish/PanShark.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Europan Shark </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openBibleFishDialog('Grouper')">
              <v-img
                src="../assets/Fish/FadedGrouper.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Grouper </span>
          </v-card-text>
        </div>
        <div class="pa-5 d-flex justify-between">
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openBibleFishDialog('Philosofish')">
              <v-img
                src="../assets/Fish/NietzschesPhilosofish.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Philosofish </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openBibleFishDialog('Piranha')">
              <v-img
                src="../assets/Fish/IonicPiranha.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Piranha </span>
          </v-card-text>
          <v-card-text
              class="d-flex text-h7 flex-column pt-8"
              style="color: #8B0000;"
            >
            <v-btn icon  @click="openBibleFishDialog('Sprat')">
              <v-img
                src="../assets/Fish/WhiteSprat.png"
                alt="Angelfish"
                max-width="75"
                max-height="75"
              />
            </v-btn>
            <span class="pt-2"> Sprat </span>
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-actions>
            <v-btn
              color="primary"
              @click="closeBibleGroupDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog v-model="bibleFishDialog" width="500px">
      <v-card style="background-color: #99d9ea">
        <v-row v-for="(fish, index) in bibleFishArray" :key="index" align="center">
          <v-col cols="6">
            <v-card-text
              class="text-h7 text-left pl-8 flex-grow-1"
              style="color: #8B0000;"
            >
              {{ fish.name }}
            </v-card-text>
          </v-col>
          <v-col cols="6">
            <v-card-actions class="pt-5">
              <v-btn icon  @click="openBibleDialog(fish.name)">
                <v-img
                  :src="getFishImage(fish.name)"
                  alt="Fish Image"
                  max-width="50"
                  max-height="50"
                />
              </v-btn>
            </v-card-actions>
          </v-col>
        </v-row>
        <div class="pa-5">
          <v-card-actions>
            <v-btn
              color="primary"
              @click="closeBibleFishDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog v-model="bibleDialog" width="500px">
      <v-card style="background-color: #99d9ea">
        <div class="d-flex">
          <v-card-text
            class="text-h6 text-right pt-8"
            style="color: #8B0000;"
          >
            {{ this.bibleDetails[0] }}
          </v-card-text>
          <v-card-text class="d-flex justify-left align-left pt-3 pb-0">
            <v-img
              :src="getFishImage(this.bibleDetails[0])"
              alt="Fish Image"
              max-width="75"
              max-height="75"
            />
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            class="text-h7 text-left pt-8"
            style="color: #8B0000;"
          >
            <b>Buy from AliFEx: </b>{{ this.bibleDetails[1] }}
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            class="text-h7 text-left pt-8"
            style="color: #8B0000;"
          >
            <b>Fertile: </b>{{ this.bibleDetails[2] }}
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            class="text-h7 text-left"
            style="color: #8B0000;"
          >
            <b> Mutation: </b>{{ this.bibleDetails[3] }}
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            class="text-h7 text-left"
            style="color: #8B0000;"
          >
            <b>Breeding:
            <span v-html="this.bibleDetails[4]"></span> </b> <br>
            <span v-html=this.bibleDetails[5]> </span>
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            class="text-h7 text-left pt-8"
            style="color: #8B0000;"
          >
            <b>Prey: </b>{{ this.bibleDetails[6] }}
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            class="text-h7 text-left"
            style="color: #8B0000;"
          >
            <b>Hunger: </b>{{ this.bibleDetails[7] }}
          </v-card-text>
        </div>
        <div class="d-flex">
          <v-card-text
            class="text-h7 text-left"
            style="color: #8B0000;"
          >
            <b>Eating Style: </b>{{ this.bibleDetails[8] }}
          </v-card-text>
        </div>
        <div class="pa-5">
          <v-card-actions>
            <v-btn
              color="primary"
              @click="closeBibleDialog"
              class="mx-auto"
            >
              Close
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
// Internal
import API from '../api/methods';
import WhiteSpratImage from '../assets/Fish/WhiteSprat.png';
import RedSpratImage from '../assets/Fish/RedSprat.png';
import GreenSpratImage from '../assets/Fish/GreenSprat.png';
import GreySpratImage from '../assets/Fish/GreySprat.png';
import RainbowSpratImage from '../assets/Fish/RainbowSprat.png';
import UVSpratImage from '../assets/Fish/UVSprat.png';
import BlueSpratImage from '../assets/Fish/BlueSprat.png';
import AcuteAngleFishImage from '../assets/Fish/AcuteAngleFish.png';
import AtomicEelImage from '../assets/Fish/AtomicEel.png';
import BermudaTriAngleImage from '../assets/Fish/BermudaTriAngleFish.png';
import BlasphemousAngleFishImage from '../assets/Fish/BlasphemousAngleFish.png';
import BlazingAngelFishImage from '../assets/Fish/BlazingAngelFish.png';
import CoruscatingAngelFishImage from '../assets/Fish/CoruscatingAngelFish.png';
import DoubleBassImage from '../assets/Fish/DoubleBass.png';
import DrummenBassImage from '../assets/Fish/DrummenBass.png';
import FadedGrouperImage from '../assets/Fish/FadedGrouper.png';
import FriendlyGrouperImage from '../assets/Fish/FriendlyGrouper.png';
import GreaterSharkImage from '../assets/Fish/GreaterShark.png';
import HeavenlyChoirfishImage from '../assets/Fish/HeavenlyChoirfish.png';
import IonicPiranhaImage from '../assets/Fish/IonicPiranha.png';
import IridescentAngelFishImage from '../assets/Fish/IridescentAngelFish.png';
import JovianPiranhaImage from '../assets/Fish/JovianPiranha.png';
import KantsPhilosofishImage from '../assets/Fish/KantsPhilosofish.png';
import LegendaryGrouperImage from '../assets/Fish/LegendaryGrouper.png';
import LesserSharkImage from '../assets/Fish/LesserShark.png';
import ManxCatfishImage from '../assets/Fish/ManxCatfish.png';
import NanoPiranhaImage from '../assets/Fish/Nano-Piranha.png';
import NietzschesPhilosofishImage from '../assets/Fish/NietzschesPhilosofish.png';
import PanSharkImage from '../assets/Fish/PanShark.png';
import ParasiticEelImage from '../assets/Fish/ParasiticEel.png';
import PiranhaEelImage from '../assets/Fish/PiranhaEel.png';
import PlatosPhilosofishImage from '../assets/Fish/PlatosPhilosofish.png';
import RecombinantEelImage from '../assets/Fish/RecombinantEel.png';
import RightAngleFishImage from '../assets/Fish/RightAngleFish.png';
import RockGrouperImage from '../assets/Fish/RockGrouper.png';
import RussellsPhilosofishImage from '../assets/Fish/RussellsPhilosofish.png';
import SchrodingersCatfishImage from '../assets/Fish/SchrodingersCatfish.png';
import SiameseCatfishImage from '../assets/Fish/SiameseCatfish.png';
import SuperGrouperImage from '../assets/Fish/SuperGrouper.png';
import SupportGrouperImage from '../assets/Fish/SupportGrouper.png';
import SwarmingEelImage from '../assets/Fish/SwarmingEel.png';
import WailingChoirfishImage from '../assets/Fish/WailingChoirfish.png';
import WalkingBassImage from '../assets/Fish/WalkingBass.png';
import WhistlingChoirfishImage from '../assets/Fish/WhistlingChoirfish.png';
import YodellingChoirfishImage from '../assets/Fish/YodellingChoirfish.png';
import InvisiblePiranhaImage from '../assets/Fish/InvisiblePiranha.png';
import BGImage from '../assets/bg.jpg';
import FrozenBGImage from '../assets/frozen_bg.png';

export default {
  name: 'HomeView',
  data: () => ({
    alert: false,
    alertColor: '',
    alertMessage: '',
    backgroundImage: BGImage,
    bibleDetails: [],
    bibleDialog: false,
    bibleGroupDialog: false,
    bibleFishDialog: false,
    bibleFishArray: [],
    breedingLog: '',
    buyFish: [],
    buyFishTypesDialog: false,
    buyFishCategoryDialog: false,
    buyFishQuantity: 0,
    buyFishRules: [
      (v) => !!v || 'Quantity is required',
      (v) => /^\d+$/.test(v) || 'Quantity must be a number',
    ],
    buySpecificFishDialog: false,
    containerVisible: true,
    currentFishIndex: 0,
    currentStep: 0,
    fishArray: [],
    fishlist: [],
    fishDialog: false,
    fishNumber: 0,
    fishPositions: {
      'Support Grouper': [0, 0],
      'Jovian Piranha': [0, 1],
      'Drummen Bass': [0, 2],
      'Friendly Grouper': [0, 3],
      'Red Sprat': [0, 4],
      'Manx Catfish': [1, 0],
      'Bermuda Tri-Angle Fish': [1, 1],
      'Russells Philosofish': [1, 2],
      'Parasitic Eel': [1, 3],
      'Greater Europan Shark': [1, 4],
      'Green Sprat': [2, 0],
      'Swarming Eel': [2, 1],
      'Heavenly Choirfish': [2, 2],
      'Nano-Piranha': [2, 3],
      'Platos Philosofish': [2, 4],
      'Iridescent Angelfish': [3, 0],
      'Whistling Choirfish': [3, 1],
      'White Sprat': [3, 2],
      'Yodelling Choirfish': [3, 3],
      'Legendary Grouper': [3, 4],
      'Kants Philosofish': [4, 0],
      'Blazing Angelfish': [4, 1],
      'Siamese Catfish': [4, 2],
      'Super Grouper': [4, 3],
      'Rainbow Sprat': [4, 4],
      'Blasphemous Angle Fish': [5, 0],
      'Lesser Europan Shark': [5, 1],
      'Grey Sprat': [5, 2],
      'Acute Angle Fish': [5, 3],
      'Wailing Choirfish': [5, 4],
      'Ultra-violet Sprat': [6, 0],
      'Blue Sprat': [6, 1],
      'Nietzsches Philosofish': [6, 2],
      'Piranha-eating Eel': [6, 3],
      'Faded Grouper': [6, 4],
      'Double Bass': [7, 0],
      'Atomic Eel': [7, 1],
      'Rock Grouper': [7, 2],
      'Walking Bass': [7, 3],
      'Right Angle Fish': [7, 4],
      'Pan Europan Shark': [8, 0],
      'Schrodingers Catfish': [8, 1],
      'Recombinant Eel': [8, 2],
      'Coruscating Angelfish': [8, 3],
      'Ionic Piranha': [8, 4],
    },
    foodLog: '',
    freezeDialog: false,
    freezeFishQuantity: 0,
    freezeFishRules: [
      (v) => !!v || 'Quantity is required',
      (v) => /^\d+$/.test(v) || 'Quantity must be a number',
    ],
    frozenFish: false,
    gridLayout: [
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
    ],
    groupedFish: {},
    kudos: 0,
    logDialog: false,
    mutationLog: '',
    originalGridLayout: [
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
      [null, null, null, null, null],
    ],
    quantity: 0,
    selectedFish: [],
    sellFishDialog: false,
    sellFishQuantity: 0,
    sellFishRules: [
      (v) => !!v || 'Quantity is required',
      (v) => /^\d+$/.test(v) || 'Quantity must be a number',
    ],
    tankDialog: false,
    totalWorth: 0,
    totalBuyWorth: 0,
    unfreezeDialog: false,
    unfreezeFishRules: [
      (v) => !!v || 'Quantity is required',
      (v) => /^\d+$/.test(v) || 'Quantity must be a number',
    ],
    unfreezeFishQuantity: 0,
    userAge: 0,
  }),
  computed: {
    rowHeight() {
    // Calculate the height of each row based on the height of the container
      const containerHeight = 716; /* Get the height of the container */
      return containerHeight / 9; // 9 rows in total
    },
    hasNextFish() {
      // Check if there is a next fish available
      return this.selectedFish.length > 1 && this.currentFishIndex < this.selectedFish.length - 1;
    },
    hasPreviousFish() {
      // Check if there is a previous fish available
      return this.selectedFish.length > 1 && this.currentFishIndex > 0;
    },
  },
  created() {
    this.getUserDetails();
    this.getFishDetails();
  },
  methods: {
    async getUserDetails() {
      const RESPONSE = await API.getUserDetails(this.$store.getters.getUserId);
      const userData = RESPONSE.data.data;
      this.kudos = userData.kudos;
      this.userAge = userData.user_age;
      this.fishNumber = userData.fish_count;
    },
    async getFishDetails() {
      const RESPONSE = await API.getFishDetailsFromUser(this.$store.getters.getUserId);
      this.fishlist = RESPONSE.data.data;
      this.groupFish();
      this.placeFishButtons();
    },
    async sellFish(frozen) {
      if (this.sellFishQuantity <= this.selectedFish[this.currentFishIndex][4]) {
        const FISHDATA = {
          user_id: this.$store.getters.getUserId,
          fish_id: this.selectedFish[this.currentFishIndex][0],
          quantity: parseInt(this.sellFishQuantity, 10),
          sell: true,
          freeze: Boolean(frozen),
        };
        const FISHRESPONSE = await API.sellFish(FISHDATA);
        if (FISHRESPONSE.data.success === true) {
          this.getFishDetails();
        }
        const costOfFish = Math.floor(this.selectedFish[this.currentFishIndex][8]);
        const kudosChange = this.sellFishQuantity * costOfFish;
        const USERDATA = {
          user_id: this.$store.getters.getUserId,
          kudos: kudosChange,
        };
        const USERRESPONSE = await API.changeKudos(USERDATA);
        if (USERRESPONSE.data.success === true) {
          this.getUserDetails();
        }
        this.fishDialog = false;
        this.sellFishDialog = false;
        this.sellFishQuantity = 1;
        this.selectedFish = [];
        this.currentFishIndex = 0;
        this.reloadContainer();
      } else {
        this.alertMessage = 'You do not have enough fish to sell this amount';
        this.alertColor = 'red';
        this.alert = true;
      }
    },
    async buyFishShop() {
      if (this.buyFishQuantity <= (Math.floor(this.kudos / this.buyFish[1]))) {
        const FISHDATA = {
          user_id: this.$store.getters.getUserId,
          name: this.buyFish[0],
          quantity: parseInt(this.buyFishQuantity, 10),
        };
        const FISHRESPONSE = await API.buyFish(FISHDATA);
        if (FISHRESPONSE.data.success === true) {
          this.getFishDetails();
        }
        const kudosChange = -1 * this.buyFishQuantity * this.buyFish[1];
        const USERDATA = {
          user_id: this.$store.getters.getUserId,
          kudos: kudosChange,
        };
        const USERRESPONSE = await API.changeKudos(USERDATA);
        if (USERRESPONSE.data.success === true) {
          this.getUserDetails();
        }
        this.buySpecificFishDialog = false;
        this.buyFishCategoryDialog = false;
        this.buyFishTypesDialog = false;
        this.buyFish = [];
        this.buyFishQuantity = 0;
        this.fishArray = [];
      } else {
        this.alertMessage = 'You do not have enough kudos to buy this many fish';
        this.alertColor = 'red';
        this.alert = true;
      }
    },
    async advanceDay() {
      const RESPONSE = await API.advanceTheDay(this.$store.getters.getUserId);
      if (RESPONSE.data.success === true) {
        this.getUserDetails();
        this.getFishDetails();
        this.breedingLog = RESPONSE.data.message.breeding_log;
        this.mutationLog = RESPONSE.data.message.mutation_log;
        this.foodLog = RESPONSE.data.message.food_log;
      }
      this.currentStep = 0;
      this.logDialog = true;
    },
    async freezeFish() {
      if (this.freezeFishQuantity <= this.selectedFish[this.currentFishIndex][4]) {
        const DATA = {
          user_id: this.$store.getters.getUserId,
          fish_id: this.selectedFish[this.currentFishIndex][0],
          quantity: parseInt(this.freezeFishQuantity, 10),
          sell: false,
          freeze: true,
        };
        const RESPONSE = await API.freezeFish(DATA);
        if (RESPONSE.data.success === true) {
          this.getFishDetails();
          this.freezeDialog = false;
          this.fishDialog = false;
          this.freezeFishQuantity = 1;
        }
      } else {
        this.alertMessage = 'You do not have enough fish to freeze this amount';
        this.alertColor = 'red';
        this.alert = true;
      }
    },
    async unfreezeFish() {
      if (this.unfreezeFishQuantity <= this.selectedFish[this.currentFishIndex][4]) {
        const DATA = {
          user_id: this.$store.getters.getUserId,
          fish_id: this.selectedFish[this.currentFishIndex][0],
          quantity: parseInt(this.unfreezeFishQuantity, 10),
          sell: false,
          freeze: false,
        };
        const RESPONSE = await API.freezeFish(DATA);
        if (RESPONSE.data.success === true) {
          this.getFishDetails();
          this.unfreezeDialog = false;
          this.fishDialog = false;
          this.unfreezeFishQuantity = 1;
        }
      } else {
        this.alertMessage = 'You do not have enough fish to defrost this amount';
        this.alertColor = 'red';
        this.alert = true;
      }
    },
    openBuySpecificFishDialog(fishName, fishPrice) {
      this.buyFish = [fishName, fishPrice];
      this.buySpecificFishDialog = true;
    },
    changeFrozenStatus() {
      if (this.selectedFish && this.selectedFish[this.currentFishIndex]) {
        if (this.selectedFish[this.currentFishIndex][9] === 0) {
          this.freezeDialog = true;
        } else {
          this.unfreezeDialog = true;
        }
      }
    },
    openFishDialog(fishCategory) {
      if (fishCategory === 'Angelfish') {
        this.fishArray.push({ name: 'Blazing Angelfish', buyPrice: 880 });
        this.fishArray.push({ name: 'Coruscating Angelfish', buyPrice: 800 });
      }
      if (fishCategory === 'Angle Fish') {
        this.fishArray.push({ name: 'Acute Angle Fish', buyPrice: 142800 });
        this.fishArray.push({ name: 'Right Angle Fish', buyPrice: 6417 });
      }
      if (fishCategory === 'Bass') {
        this.fishArray.push({ name: 'Double Bass', buyPrice: 142800 });
        this.fishArray.push({ name: 'Walking Bass', buyPrice: 5337 });
      }
      if (fishCategory === 'Catfish') {
        this.fishArray.push({ name: 'Manx Catfish', buyPrice: 6000 });
        this.fishArray.push({ name: 'Siamese Catfish', buyPrice: 1867 });
      }
      if (fishCategory === 'Choirfish') {
        this.fishArray.push({ name: 'Wailing Choirfish', buyPrice: 29500 });
        this.fishArray.push({ name: 'Whistling Choirfish', buyPrice: 24400 });
        this.fishArray.push({ name: 'Yodelling Choirfish', buyPrice: 700134 });
      }
      if (fishCategory === 'Eel') {
        this.fishArray.push({ name: 'Parasitic Eel', buyPrice: 65334 });
        this.fishArray.push({ name: 'Recombinant Eel', buyPrice: 3500 });
        this.fishArray.push({ name: 'Swarming Eel', buyPrice: 13260 });
        this.fishArray.push({ name: 'Piranha-eating Eel', buyPrice: 5500 });
      }
      if (fishCategory === 'Europan Shark') {
        this.fishArray.push({ name: 'Greater Europan Shark', buyPrice: 140000 });
        this.fishArray.push({ name: 'Lesser Europan Shark', buyPrice: 8400 });
      }
      if (fishCategory === 'Grouper') {
        this.fishArray.push({ name: 'Friendly Grouper', buyPrice: 120000 });
        this.fishArray.push({ name: 'Rock Grouper', buyPrice: 308000 });
        this.fishArray.push({ name: 'Support Grouper', buyPrice: 322000 });
      }
      if (fishCategory === 'Philosofish') {
        this.fishArray.push({ name: 'Kants Philosofish', buyPrice: 7276 });
        this.fishArray.push({ name: 'Platos Philosofish', buyPrice: 260 });
        this.fishArray.push({ name: 'Russells Philosofish', buyPrice: 2774 });
      }
      if (fishCategory === 'Piranha') {
        this.fishArray.push({ name: 'Ionic Piranha', buyPrice: 306 });
        this.fishArray.push({ name: 'Jovian Piranha', buyPrice: 8540 });
        this.fishArray.push({ name: 'Nano-Piranha', buyPrice: 24 });
      }
      if (fishCategory === 'Sprat') {
        this.fishArray.push({ name: 'White Sprat', buyPrice: 2 });
        this.fishArray.push({ name: 'Red Sprat', buyPrice: 29 });
        this.fishArray.push({ name: 'Green Sprat', buyPrice: 33 });
        this.fishArray.push({ name: 'Blue Sprat', buyPrice: 51 });
        this.fishArray.push({ name: 'Grey Sprat', buyPrice: 60 });
      }
      this.buyFishCategoryDialog = true;
    },
    openBibleFishDialog(fishCategory) {
      if (fishCategory === 'Angelfish') {
        this.bibleFishArray.push({ name: 'Blazing Angelfish' });
        this.bibleFishArray.push({ name: 'Coruscating Angelfish' });
        this.bibleFishArray.push({ name: 'Iridescent Angelfish' });
      }
      if (fishCategory === 'Angle Fish') {
        this.bibleFishArray.push({ name: 'Acute Angle Fish' });
        this.bibleFishArray.push({ name: 'Blasphemous Angle Fish' });
        this.bibleFishArray.push({ name: 'Bermuda Tri-Angle Fish' });
        this.bibleFishArray.push({ name: 'Right Angle Fish' });
      }
      if (fishCategory === 'Bass') {
        this.bibleFishArray.push({ name: 'Double Bass' });
        this.bibleFishArray.push({ name: 'Drummen Bass' });
        this.bibleFishArray.push({ name: 'Walking Bass' });
      }
      if (fishCategory === 'Catfish') {
        this.bibleFishArray.push({ name: 'Manx Catfish' });
        this.bibleFishArray.push({ name: 'Siamese Catfish' });
        this.bibleFishArray.push({ name: 'Schrodingers Catfish' });
      }
      if (fishCategory === 'Choirfish') {
        this.bibleFishArray.push({ name: 'Wailing Choirfish' });
        this.bibleFishArray.push({ name: 'Whistling Choirfish' });
        this.bibleFishArray.push({ name: 'Yodelling Choirfish' });
        this.bibleFishArray.push({ name: 'Heavenly Choirfish' });
      }
      if (fishCategory === 'Eel') {
        this.bibleFishArray.push({ name: 'Atomic Eel' });
        this.bibleFishArray.push({ name: 'Parasitic Eel' });
        this.bibleFishArray.push({ name: 'Recombinant Eel' });
        this.bibleFishArray.push({ name: 'Swarming Eel' });
        this.bibleFishArray.push({ name: 'Piranha-eating Eel' });
      }
      if (fishCategory === 'Europan Shark') {
        this.bibleFishArray.push({ name: 'Greater Europan Shark' });
        this.bibleFishArray.push({ name: 'Lesser Europan Shark' });
        this.bibleFishArray.push({ name: 'Pan Europan Shark' });
      }
      if (fishCategory === 'Grouper') {
        this.bibleFishArray.push({ name: 'Faded Grouper' });
        this.bibleFishArray.push({ name: 'Friendly Grouper' });
        this.bibleFishArray.push({ name: 'Legendary Grouper' });
        this.bibleFishArray.push({ name: 'Rock Grouper' });
        this.bibleFishArray.push({ name: 'Super Grouper' });
        this.bibleFishArray.push({ name: 'Support Grouper' });
      }
      if (fishCategory === 'Philosofish') {
        this.bibleFishArray.push({ name: 'Kants Philosofish' });
        this.bibleFishArray.push({ name: 'Nietzsches Philosofish' });
        this.bibleFishArray.push({ name: 'Platos Philosofish' });
        this.bibleFishArray.push({ name: 'Russells Philosofish' });
      }
      if (fishCategory === 'Piranha') {
        this.bibleFishArray.push({ name: 'Ionic Piranha' });
        this.bibleFishArray.push({ name: 'Invisible Piranha' });
        this.bibleFishArray.push({ name: 'Jovian Piranha' });
        this.bibleFishArray.push({ name: 'Nano-Piranha' });
      }
      if (fishCategory === 'Sprat') {
        this.bibleFishArray.push({ name: 'White Sprat' });
        this.bibleFishArray.push({ name: 'Red Sprat' });
        this.bibleFishArray.push({ name: 'Green Sprat' });
        this.bibleFishArray.push({ name: 'Blue Sprat' });
        this.bibleFishArray.push({ name: 'Grey Sprat' });
        this.bibleFishArray.push({ name: 'Rainbow Sprat' });
        this.bibleFishArray.push({ name: 'Ultra-violet Sprat' });
      }
      this.bibleFishDialog = true;
    },
    affordFishQuantity() {
      const quantity = Math.floor(this.kudos / this.buyFish[1]);
      return quantity;
    },
    sellFishWorth() {
      if (this.selectedFish && this.selectedFish[this.currentFishIndex]) {
        const quantity = this.sellFishQuantity || 0;
        const pricePerUnit = Math.floor(this.selectedFish[this.currentFishIndex][8]) || 0;
        this.totalWorth = quantity * pricePerUnit;
      } else {
        this.totalWorth = 0;
      }
      return this.totalWorth;
    },
    buyFishWorth() {
      const quantity = this.buyFishQuantity || 0;
      const pricePerUnit = this.buyFish[1] || 0;
      this.totalBuyWorth = quantity * pricePerUnit;
      return this.totalBuyWorth;
    },
    calculateSchools() {
      let numberOfGroupsFrozen = 0;
      let numberOfGroupsUnfrozen = 0;
      const groupedSchoolFrozen = {};
      const groupedSchoolUnfrozen = {};

      if (this.fishlist && this.fishlist.length > 0) {
        this.fishlist.forEach((fishlist) => {
          const fishName = fishlist[2];
          const fishAge = fishlist[5];
          const isFrozen = fishlist[9];
          const isFrozenBool = Boolean(isFrozen);

          const groupKey = `${fishName}_${fishAge}`;
          if (isFrozenBool) {
            if (!groupedSchoolFrozen[groupKey]) {
              groupedSchoolFrozen[groupKey] = [];
              numberOfGroupsFrozen += 1;
            }
            groupedSchoolFrozen[groupKey].push(fishlist);
          } else {
            if (!groupedSchoolUnfrozen[groupKey]) {
              groupedSchoolUnfrozen[groupKey] = [];
              numberOfGroupsUnfrozen += 1;
            }
            groupedSchoolUnfrozen[groupKey].push(fishlist);
          }
        });
      }
      return numberOfGroupsFrozen + numberOfGroupsUnfrozen;
    },
    groupFish() {
      this.groupedFish = {};
      if (this.fishlist && this.fishlist.length > 0) {
        this.fishlist.forEach((fishlist) => {
          const fishName = fishlist[2];
          const isFrozen = fishlist[9];
          const isFrozenBool = Boolean(isFrozen);
          if (this.frozenFish === isFrozenBool) {
            if (!this.groupedFish[fishName]) {
              this.groupedFish[fishName] = [];
            }
            this.groupedFish[fishName].push(fishlist);
          }
        });
        Object.keys(this.groupedFish).forEach((fishName) => {
          const fishGroup = this.groupedFish[fishName];
          fishGroup.sort((a, b) => a[5] - b[5]);
        });
      }
    },
    calculateValue() {
      let totalValue = 0;

      if (this.fishlist && this.fishlist.length > 0) {
        this.fishlist.forEach((fishlist) => {
          const quantity = fishlist[4];
          const value = fishlist[8];

          totalValue += quantity * value;
        });
      }
      return totalValue;
    },
    openSellFishDialog() {
      this.fishDialog = false;
      this.sellFishDialog = true;
    },
    closeSellFishDialog() {
      this.fishDialog = true;
      this.sellFishDialog = false;
    },
    closeBibleFishDialog() {
      this.bibleFishDialog = false;
      this.bibleFishArray = [];
    },
    closeBuyFishDialog() {
      this.buySpecificFishDialog = false;
      this.buyFishCategoryDialog = true;
    },
    showFishDetails(name) {
      this.selectedFish = this.groupedFish[name] || [];
      this.fishDialog = true;
    },
    showBibleGroup() {
      this.bibleGroupDialog = true;
    },
    closeBibleGroupDialog() {
      this.bibleGroupDialog = false;
    },
    closeFishDialog() {
      this.selectedFish = [];
      this.fishDialog = false;
      this.currentFishIndex = 0;
    },
    openBibleDialog(fishName) {
      this.bibleDetails = API.getBibleDetails(fishName);
      this.bibleDialog = true;
    },
    closeLogDialog() {
      this.logDialog = false;
    },
    showTankDialog() {
      this.tankDialog = true;
    },
    closeTankDialog() {
      this.tankDialog = false;
    },
    closeFreezeDialog() {
      this.freezeDialog = false;
    },
    closeUnfreezeDialog() {
      this.unfreezeDialog = false;
    },
    showBuy() {
      this.buyFishTypesDialog = true;
    },
    closeBuyFishTypesDialog() {
      this.buyFishTypesDialog = false;
    },
    closeBuyFishCategoryDialog() {
      this.buyFishCategoryDialog = false;
      this.fishArray = [];
    },
    closeBibleDialog() {
      this.bibleDialog = false;
    },
    showNextFish() {
      // Increment the current index to display the next fish
      this.currentFishIndex = (this.currentFishIndex + 1) % this.selectedFish.length;
    },
    showPreviousFish() {
    // Decrement the current index to display the previous fish
      this.currentFishIndex = (
        this.currentFishIndex - 1 + this.selectedFish.length
      ) % this.selectedFish.length;
    },
    showTank() {
      this.frozenFish = false;
      this.getFishDetails();
      this.backgroundImage = BGImage;
      this.reloadContainer();
    },
    showFrozenTank() {
      this.frozenFish = true;
      this.getFishDetails();
      this.backgroundImage = FrozenBGImage;
      this.reloadContainer();
    },
    getFishImage(name) {
      const imageMapping = {
        'White Sprat': WhiteSpratImage,
        'Red Sprat': RedSpratImage,
        'Green Sprat': GreenSpratImage,
        'Grey Sprat': GreySpratImage,
        'Rainbow Sprat': RainbowSpratImage,
        'Ultra-violet Sprat': UVSpratImage,
        'Blue Sprat': BlueSpratImage,
        'Yodelling Choirfish': YodellingChoirfishImage,
        'Whistling Choirfish': WhistlingChoirfishImage,
        'Walking Bass': WalkingBassImage,
        'Wailing Choirfish': WailingChoirfishImage,
        'Swarming Eel': SwarmingEelImage,
        'Support Grouper': SupportGrouperImage,
        'Super Grouper': SuperGrouperImage,
        'Siamese Catfish': SiameseCatfishImage,
        'Schrodingers Catfish': SchrodingersCatfishImage,
        'Russells Philosofish': RussellsPhilosofishImage,
        'Rock Grouper': RockGrouperImage,
        'Right Angle Fish': RightAngleFishImage,
        'Recombinant Eel': RecombinantEelImage,
        'Parasitic Eel': ParasiticEelImage,
        'Piranha-eating Eel': PiranhaEelImage,
        'Nietzsches Philosofish': NietzschesPhilosofishImage,
        'Platos Philosofish': PlatosPhilosofishImage,
        'Pan Europan Shark': PanSharkImage,
        'Nano-Piranha': NanoPiranhaImage,
        'Manx Catfish': ManxCatfishImage,
        'Lesser Europan Shark': LesserSharkImage,
        'Legendary Grouper': LegendaryGrouperImage,
        'Kants Philosofish': KantsPhilosofishImage,
        'Jovian Piranha': JovianPiranhaImage,
        'Iridescent Angelfish': IridescentAngelFishImage,
        'Heavenly Choirfish': HeavenlyChoirfishImage,
        'Ionic Piranha': IonicPiranhaImage,
        'Greater Europan Shark': GreaterSharkImage,
        'Friendly Grouper': FriendlyGrouperImage,
        'Faded Grouper': FadedGrouperImage,
        'Drummen Bass': DrummenBassImage,
        'Double Bass': DoubleBassImage,
        'Coruscating Angelfish': CoruscatingAngelFishImage,
        'Blazing Angelfish': BlazingAngelFishImage,
        'Blasphemous Angle Fish': BlasphemousAngleFishImage,
        'Bermuda Tri-Angle Fish': BermudaTriAngleImage,
        'Atomic Eel': AtomicEelImage,
        'Acute Angle Fish': AcuteAngleFishImage,
        'Invisible Piranha': InvisiblePiranhaImage,
      };

      // Check if the name exists in the mapping, return the corresponding image URL
      if (name in imageMapping) {
        return imageMapping[name];
      }
      return WhiteSpratImage;
    },
    placeFishButtons() {
      const newGridLayout = JSON.parse(JSON.stringify(this.originalGridLayout));
      this.gridLayout = newGridLayout;
      Object.keys(this.groupedFish).forEach((fishName) => {
        const position = this.fishPositions[fishName];
        if (position) {
          const [row, col] = position;
          if (this.gridLayout[row] && this.gridLayout[row][col] === null) {
            this.gridLayout[row].splice(col, 1, fishName);
          }
        }
      });
    },
    reloadContainer() {
      // Toggle the visibility of the container to trigger a re-render
      this.containerVisible = false;
      this.$nextTick(() => {
        this.containerVisible = true;
      });
    },
    nextStep() {
      if (this.currentStep < 2) {
        this.currentStep += 1;
      }
    },
    previousStep() {
      if (this.currentStep > 0) {
        this.currentStep -= 1;
      }
    },
    getCurrentLog() {
      let log = '';
      if (this.currentStep === 0) {
        log = this.foodLog;
      } else if (this.currentStep === 1) {
        log = this.breedingLog;
      } else if (this.currentStep === 2) {
        log = this.mutationLog;
      }
      return log;
    },
  },
};
</script>

<style scoped>
.grid-cell {
  height: 100%;
}
.grid-container {
  margin: 0; /* Reset margin */
  padding: 0; /* Reset padding */
  background-repeat: no-repeat;
  background-size: 100% auto;
  background-position: center;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
}
.no-margin {
  margin: 0 !important;
  padding: 0;
}
.first-row-padding {
  padding-top: 10px !important;
}
.first-col-padding {
  padding-left: 10px !important;
}
</style>

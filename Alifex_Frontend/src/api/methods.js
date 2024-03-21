import axios from 'axios';

const API_URL = process.env.VUE_APP_API_URL;

export default {
  /**
   * Creates a user account by making a call to the Codeium api.
   * @param  { Object } data - Request body data.
   * @return { Function } apiCall - API call function
   */
  createAccount(data) {
    return this.apiCall(`${API_URL}/user`, 'POST', data);
  },
  loginUser(data) {
    return this.apiCall(`${API_URL}/login`, 'POST', data);
  },
  getUserDetails(userId) {
    return this.apiCall(`${API_URL}/user/id/${userId}`, 'GET', {});
  },
  getFishDetailsFromUser(userId) {
    return this.apiCall(`${API_URL}/fish/id/${userId}`, 'GET', {});
  },
  sellFish(data) {
    return this.apiCall(`${API_URL}/fish`, 'PATCH', data);
  },
  changeKudos(data) {
    return this.apiCall(`${API_URL}/user`, 'PATCH', data);
  },
  advanceTheDay(userId) {
    return this.apiCall(`${API_URL}/game/${userId}`, 'GET', {});
  },
  freezeFish(data) {
    return this.apiCall(`${API_URL}/fish`, 'PATCH', data);
  },
  buyFish(data) {
    return this.apiCall(`${API_URL}/fish`, 'POST', data);
  },
  /**
   * Makes a call to the Codeium api.
   * @param  { String } url - The API url.
   * @param  { String } method  - HTTP request method.
   * @param  { Object } data - Request body data.
   * @return { Object } REPONSE - The API call response
   */
  async apiCall(url, method, data) {
    let error = null;
    const RESPONSE = await axios({
      url,
      method,
      data,
    }).catch((e) => {
      error = e;
    });
    return RESPONSE || error.response;
  },
  getBibleDetails(fishName) {
    const bibleDetails = [];
    if (fishName === 'White Sprat') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Sterile'); // Fertile
      bibleDetails.push('Day 3: 33% chance: Red Sprat (1-1), 33% chance: Green Sprat (1-1), 34% chance Blue Sprat (1-1)'); // Mutation
      bibleDetails.push(''); // Breeding Preferred
      bibleDetails.push('Sterile'); // Breeding
      bibleDetails.push('None'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('n/a'); // Eating Style
    }
    if (fishName === 'Red Sprat') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 9: Grey Sprat (1-1)'); // Mutation
      bibleDetails.push('Red Sprat => White Sprat'); // Breeding Preferred
      bibleDetails.push('Blue Sprat => Green Sprat <br> Green Sprat => Blue Sprat'); // Breeding
      bibleDetails.push('None'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('n/a'); // Eating Style
    }
    if (fishName === 'Green Sprat') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 5: Grey Sprat (1-1)'); // Mutation
      bibleDetails.push('Green Sprat => White Sprat'); // Breeding Preferred
      bibleDetails.push('Blue Sprat => Red Sprat <br> Red Sprat => Blue Sprat'); // Breeding
      bibleDetails.push('None'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('n/a'); // Eating Style
    }
    if (fishName === 'Blue Sprat') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 7: Grey Sprat (1-1)'); // Mutation
      bibleDetails.push('Blue Sprat => White Sprat'); // Breeding Preferred
      bibleDetails.push('Red Sprat => Green Sprat <br> Green Sprat => Red Sprat'); // Breeding
      bibleDetails.push('None'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('n/a'); // Eating Style
    }
    if (fishName === 'Grey Sprat') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Sterile'); // Fertile
      bibleDetails.push('Day 6: 25% chance: dies, 75% chance: Rainbow Sprat (1-1)'); // Mutation
      bibleDetails.push(''); // Breeding Preferred
      bibleDetails.push('Sterile'); // Breeding
      bibleDetails.push('None'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('n/a'); // Eating Style
    }
    if (fishName === 'Rainbow Sprat') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 3: 40% chance: Ultra-violet Sprat (school), 20% chance: Lesser Europan Shark (school), 20% chance: Coruscating Angelfish (school), 20% chance: Siamese Catfish (school)'); // Mutation
      bibleDetails.push('Blazing Angelfish => Iridescent Angelfish'); // Breeding Preferred
      bibleDetails.push(''); // Breeding
      bibleDetails.push('White Sprat'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Ultra-violet Sprat') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 3: 10% chance: Whistling Choirfish (1-1), 10% chance: Platos Philosofish (1-1), 10% chance: Walking Bass (1-1), 10% chance: Jovian Piranha, 10% chance: Right Angle Fish (1-1), 10% chance: Friendly Grouper (school), 40% chance: Rainbow Sprat (school)'); // Mutation
      bibleDetails.push('Wailing Choirfish => Yodelling Choirfish'); // Breeding Preferred
      bibleDetails.push(''); // Breeding
      bibleDetails.push('Rainbow Sprat'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Blazing Angelfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 9'); // Fertile
      bibleDetails.push('Day 13: dies'); // Mutation
      bibleDetails.push('Rainbow Sprat => Iridescent Angelfish'); // Breeding Preferred
      bibleDetails.push('Blazing Angelfish => Blazing Angelfish <br> Whistling Choirfish => Coruscating Angelfish <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, Yodelling Choirfish'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Coruscating Angelfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 9'); // Fertile
      bibleDetails.push('Day 13: Blazing Angelfish (school)'); // Mutation
      bibleDetails.push('Coruscating Angelfish => Coruscating Angelfish'); // Breeding Preferred
      bibleDetails.push('Whistling Choirfish => Coruscating Angelfish <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, all Eel'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Iridescent Angelfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 7: Coruscating Angelfish (school)'); // Mutation
      bibleDetails.push('Iridescent Angelfish => Iridescent Angelfish'); // Breeding Preferred
      bibleDetails.push('Yodelling Choirfish => Heavenly Choirfish <br> Whistling Choirfish => Coruscating Angelfish <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Angle Fish'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Acute Angle Fish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 9'); // Fertile
      bibleDetails.push('Day 23: 50% chance: dies, 50% chance: Whistling Choirfish (school)'); // Mutation
      bibleDetails.push('Acute Angle Fish => Acute Angle Fish'); // Breeding Preferred
      bibleDetails.push('Yodelling Choirfish => Whistling Choirfish <br> Whistling Choirfish => Whistling Choirfish <br> Wailing Choirfish => Whistling Choirfish <br> Walking Bass => Walking Bass <br> Drummen Bass => Walking Bass <br> Double Bass => Walking Bass <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Bermuda Tri-Angle Fish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 7'); // Fertile
      bibleDetails.push('Day 13: 50% chance: dies, 50% chance: Bermuda Tri-Angle Fish (school)'); // Mutation
      bibleDetails.push(''); // Breeding Preferred
      bibleDetails.push('Sterile'); // Breeding
      bibleDetails.push('All Sprat, Jovian Piranha, Russells Philosofish, Lesser Europan Shark, all Catfish, Acute Angle Fish, Right Angle Fish'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Blasphemous Angle Fish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 3'); // Fertile
      bibleDetails.push('Day 6: dies'); // Mutation
      bibleDetails.push('Blasphemous Angle Fish => Bermuda Tri-Angle Fish'); // Breeding Preferred
      bibleDetails.push('Atomic Eel => Atomic Eel <br> Wailing Choirfish => Yodelling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, Jovian Piranha, Russells Philosofish, Lesser Europan Shark, all Catfish, Acute Angle Fish, Right Angle Fish'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Right Angle Fish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 5'); // Fertile
      bibleDetails.push('Day 17: 50% chance: White Sprat (school), 50% chance Acute Angle Fish (1-1)'); // Mutation
      bibleDetails.push('<br>Lesser Europan Shark => Right Angle Fish <br> Greater Europan Shark => Right Angle Fish <br> Pan Europan Shark => Right Angle Fish <br> Coruscating Angelfish => Right Angle Fish <br> Blazing Angelfish => Right Angle Fish <br> Iridescent Angelfish => Right Angle Fish <br> Whistling Choirfish => Right Angle Fish <br> Wailing Choirfish => Right Angle Fish <br> Yodelling Choirfish => Right Angle Fish <br> Siamese Catfish => Right Angle Fish <br> Manx Catfish => Right Angle Fish <br> Walking Bass => Right Angle Fish <br> Drummen Bass => Right Angle Fish <br> Double Bass => Right Angle Fish <br> Jovian Piranha => Right Angle Fish <br> Ionic Piranha => Right Angle Fish <br> Nano-Piranha => Right Angle Fish <br> Recombinant Eel => Right Angle Fish <br> Swarming Eel => Right Angle Fish <br> Parasitic Eel => Right Angle Fish <br> Piranha-eating Eel => Right Angle Fish <br> Atomic Eel => Right Angle Fish <br> Right Angle Fish => Right Angle Fish <br> Acute Angle Fish => Right Angle Fish <br> Blasphemous Angle Fish => Right Angle Fish <br> Friendly Grouper => Right Angle Fish <br> Support Grouper => Right Angle Fish <br> Rock Grouper => Right Angle Fish <br> Legendary Grouper => Right Angle Fish <br> Platos Philosofish => Right Angle Fish <br> Russells Philosofish => Right Angle Fish <br> Kants Philosofish => Right Angle Fish'); // Breeding Preferred
      bibleDetails.push('Whistling Choirfish => Wailing Choirfish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Double Bass') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 17'); // Fertile
      bibleDetails.push('Day 23: Blazing Angelfish (school)'); // Mutation
      bibleDetails.push('Double Bass => Drummen Bass'); // Breeding Preferred
      bibleDetails.push('Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Acute Angle Fish => Walking Bass <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Drummen Bass') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 13'); // Fertile
      bibleDetails.push('Day 43: Blasphemous Angle Fish (1-1)'); // Mutation
      bibleDetails.push('Drummen Bass => Super Grouper'); // Breeding Preferred
      bibleDetails.push('Rock Grouper => Super Grouper <br> Support Grouper => Jovian Piranha <br> Jovian Piranha => Atomic Eel <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Acute Angle Fish => Walking Bass <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Philosofish, Lesser Europan Shark, all Choirfish, all Catfish, all Angelfish'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Walking Bass') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 7'); // Fertile
      bibleDetails.push('Day 13: Siamese Catfish (school)'); // Mutation
      bibleDetails.push('Walking Bass => Walking Bass '); // Breeding Preferred
      bibleDetails.push('Friendly Grouper => Double Bass <br> Rock Grouper => Double Bass <br> Support Grouper => Double Bass <br> Legendary Grouper => Double Bass <br> Siamese Catfish => Walking Bass <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Acute Angle Fish => Walking Bass <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Manx Catfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 5'); // Fertile
      bibleDetails.push('Day 9: 10% chance: Siamese Catfish (school), 10% chance: Jovian Piranha (school), 10% chance: Recombinant Eel (school), 10% chance: Schrodingers Catfish (1-1), 10% chance: Friendly Grouper (1-1), 50% chance: dies'); // Mutation
      bibleDetails.push('Manx Catfish => Siamese Catfish '); // Breeding Preferred
      bibleDetails.push('Jovian Piranha => Russells Philosofish <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Acute Angle Fish => Walking Bass <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Schrodingers Catfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Sterile'); // Fertile
      bibleDetails.push('None'); // Mutation
      bibleDetails.push('Friendly Grouper => Bermuda Tri-Angle Fish'); // Breeding Preferred
      bibleDetails.push(''); // Breeding
      bibleDetails.push('All Sprat'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Siamese Catfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 7'); // Fertile
      bibleDetails.push('Day 11: Walking Bass (school)'); // Mutation
      bibleDetails.push('Siamese Catfish => Manx Catfish'); // Breeding Preferred
      bibleDetails.push('Walking Bass => Siamese Catfish <br> Wailing Choirfish => Whistling Choirfish <br> Jovian Piranha => Russells Philosofish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Heavenly Choirfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Sterile'); // Fertile
      bibleDetails.push('Day 3: dies'); // Mutation
      bibleDetails.push(''); // Breeding Preferred
      bibleDetails.push('Sterile'); // Breeding
      bibleDetails.push('All Piranha, all Europan Shark, all Eel, Bermuda Tri-Angle Fish, Blasphemous Angle Fish'); // Prey
      bibleDetails.push('Unknown'); // Hunger
      bibleDetails.push('Unknown'); // Eating Style
    }
    if (fishName === 'Wailing Choirfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 9'); // Fertile
      bibleDetails.push('Day 11: dies'); // Mutation
      bibleDetails.push('Wailing Choirfish => Wailing Choirfish'); // Breeding Preferred
      bibleDetails.push('Blasphemous Angle Fish => Yodelling Choirfish <br> Ultra-violet Sprat => Yodelling Choirfish <br> Ionic Piranha => Recombinant Eel <br> Acute Angle Fish => Whistling Choirfish <br> Nietzsches Philosofish => Yodelling Choirfish <br> Lesser Europan Shark => Whistling Choirfish <br> Greater Europan Shark => Whistling Choirfish <br> Pan Europan Shark => Whistling Choirfish <br> Coruscating Angelfish => Whistling Choirfish <br> Blazing Angelfish => Whistling Choirfish <br> Iridescent Angelfish => Whistling Choirfish <br> Siamese Catfish => Whistling Choirfish <br> Manx Catfish => Whistling Choirfish <br> Schrodingers Catfish => Whistling Choirfish <br> Walking Bass => Whistling Choirfish <br> Drummen Bass => Whistling Choirfish <br> Double Bass => Whistling Choirfish <br> Jovian Piranha => Whistling Choirfish <br> Nano-Piranha => Whistling Choirfish <br> Invisible Piranha => Whistling Choirfish <br> Right Angle Fish => Whistling Choirfish <br> Bermuda Tri-Angle Fish => Whistling Choirfish <br> Friendly Grouper => Whistling Choirfish <br> Support Gruper => Whistling Choirfish <br> Rock Grouper => Whistling Choirfish <br> Legendary Grouper => Whistling Choirfish <br> Platos Philosofish => Whistling Choirfish <br> Russells Philosofish => Whistling Choirfish <br> Kants Philosofish => Whistling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, all Catfish'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Whistling Choirfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 7'); // Fertile
      bibleDetails.push('Day 23: 50% chance: dies, 25% chance: Grey Sprat (1-1), 25% chance: Wailing Choirfish (1-1)'); // Mutation
      bibleDetails.push('Whistling Choirfish => Whistling Choirfish'); // Breeding Preferred
      bibleDetails.push('Coruscating Angelfish => Coruscating Angelfish <br> Blazing Angelfish => Coruscating Angelfish <br> Iridescent Angelfish => Coruscating Angelfish <br> Right Angle Fish => Right Angle Fish <br> Acute Angle Fish => Whistling Choirfish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, all Catfish'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Yodelling Choirfish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 5'); // Fertile
      bibleDetails.push('Day 13: Wailing Choirfish (1-1)'); // Mutation
      bibleDetails.push('Yodelling Choirfish => Yodelling Choirfish'); // Breeding Preferred
      bibleDetails.push('Iridescent Angelfish => Heavenly Choirfish <br> Right Angle Fish => Right Angle Fish <br> Acute Angle Fish => Whistling Choirfish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('Wailing Choirfish, Whistling Choirfish, all Catfish'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Atomic Eel') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 3'); // Fertile
      bibleDetails.push('None'); // Mutation
      bibleDetails.push('Blasphemous Angle Fish => Atomic Eel'); // Breeding Preferred
      bibleDetails.push('Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('Atomic Eel'); // Prey
      bibleDetails.push('100% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Parasitic Eel') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 4'); // Fertile
      bibleDetails.push('Day 10: 80 chance: dies, 10% chance: Recombinant Eel (school), 10% chance: Piranha-eating Eel (school)'); // Mutation
      bibleDetails.push('Parasitic Eel => Parasitic Eel'); // Breeding Preferred
      bibleDetails.push('Recombinant Eel => Parasitic Eel <br> Swarming Eel => Parasitic Eel <br> Piranha-eating Eel => Piranha-eating Eel <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, all Philosofish, Support Grouper, Friendly Grouper, all Choirfish, all Catfish, all Bass, Right Angle Fish, all Angelfish'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Piranha-eating Eel') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 9'); // Fertile
      bibleDetails.push('None'); // Mutation
      bibleDetails.push('Piranha-eating Eel => Atomic Eel'); // Breeding Preferred
      bibleDetails.push('Recombinant Eel => Piranha-eating Eel <br> Swarming Eel => Piranha-eating Eel <br> Parasitic Eel => Piranha-eating Eel <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Piranha'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Recombinant Eel') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 4'); // Fertile
      bibleDetails.push('Day 10: 80% chance: dies, 20% chance: Swarming Eel (school)'); // Mutation
      bibleDetails.push('Recombinant Eel => Recombinant Eel'); // Breeding Preferred
      bibleDetails.push('Piranha-eating Eel => Piranha-eating Eel <br> Swarming Eel => Swarming Eel <br> Parasitic Eel => Parasitic Eel <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, All Bass'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Swarming Eel') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 4'); // Fertile
      bibleDetails.push('Day 10: 80% chance: dies, 10% chance: Recombinant Eel (school), 10% chance: Parasitic Eel (1-1)'); // Mutation
      bibleDetails.push('Swarming Eel => Swarming Eel'); // Breeding Preferred
      bibleDetails.push('Piranha-eating Eel => Piranha-eating Eel <br> Recombinant Eel => Swarming Eel <br> Parasitic Eel => Parasitic Eel <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, All Bass'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Greater Europan Shark') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 16'); // Fertile
      bibleDetails.push('Day 19: dies'); // Mutation
      bibleDetails.push('Lesser Europan Shark => Lesser Europan Shark'); // Breeding Preferred
      bibleDetails.push('Greater Europan Shark => Pan Europan Shark <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, all Bass, all Philosofish, all Grouper, all Eel, all Choirfish, all Catfish, all Angle Fish, all Angelfish'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Lesser Europan Shark') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 9'); // Fertile
      bibleDetails.push('Day 12: dies'); // Mutation
      bibleDetails.push('Lesser Europan Shark => Greater Europan Shark'); // Breeding Preferred
      bibleDetails.push('Greater Europan Shark => Lesser Europan Shark <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, all Philosofish, all Catfish, Coruscating Angelfish'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Pan Europan Shark') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 2'); // Fertile
      bibleDetails.push('Day 25: dies'); // Mutation
      bibleDetails.push('Pan Europan Shark => Pan Europan Shark'); // Breeding Preferred
      bibleDetails.push('Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, all Philosofish, all Catfish, all Piranha, all Grouper, all Europan Shark, all Eel, all Choirfish, all Bass, all Angle Fish, all Angelfish'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Faded Grouper') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Sterile'); // Fertile
      bibleDetails.push('Day 56: dies'); // Mutation
      bibleDetails.push(''); // Breeding Preferred
      bibleDetails.push('Sterile'); // Breeding
      bibleDetails.push('White Sprat'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Friendly Grouper') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 10'); // Fertile
      bibleDetails.push('Day 19: 80% chance: dies, 20% chance: Jovian Piranha (school)'); // Mutation
      bibleDetails.push('Friendly Grouper => Support Grouper'); // Breeding Preferred
      bibleDetails.push('Legendary Grouper => Super Grouper <br> Schrodingers Catfish => Bermuda Tri-Angle Fish <br> Walking Bass => Double Bass <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('All Sprat, all Eel'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Legendary Grouper') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 16: 90% chance: dies, 10% chance: Heavenly Choirfish (school)'); // Mutation
      bibleDetails.push('Friendly Grouper => Super Grouper'); // Breeding Preferred
      bibleDetails.push('Support Grouper => Super Grouper <br> Rock Grouper => Super Grouper <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('Lesser Europan Shark, all Bass'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Rock Grouper') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 3'); // Fertile
      bibleDetails.push('Day 6: 80% chance: dies, 20% chance: Super Grouper (1-1)'); // Mutation
      bibleDetails.push('Rock Grouper => Rock Grouper'); // Breeding Preferred
      bibleDetails.push('Support Grouper => Walking Bass <br> Legendary Grouper => Super Grouper <br> Walking Bass => Double Bass <br> Drummen Bass => Super Grouper <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('all Sprat, All Eel'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Super Grouper') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Sterile'); // Fertile
      bibleDetails.push('Day 6: 10% chance: dies, 35% chance: Faded Grouper (1-1), 5% chance: Legendary Grouper (1-1), 20% chance: Rock Grouper (school), 10% chance: Support Grouper (school), 10% chance: Platos Philosofish (school), 10% chance: Blasphemous Angle Fish (school)'); // Mutation
      bibleDetails.push(''); // Breeding Preferred
      bibleDetails.push('Sterile'); // Breeding
      bibleDetails.push('all Europan Shark'); // Prey
      bibleDetails.push('20% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Support Grouper') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 7'); // Fertile
      bibleDetails.push('Day 26: 80% chance: dies, 20% chance: Ionic Piranha (school)'); // Mutation
      bibleDetails.push('Support Grouper => Rock Grouper'); // Breeding Preferred
      bibleDetails.push('Legendary Grouper => Super Grouper <br> Rock Grouper => Walking Bass <br> Walking Bass => Double Bass <br> Drummen Bass => Jovian Piranha <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('all Sprat, all Eel'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Smallest suitable prey'); // Eating Style
    }
    if (fishName === 'Kants Philosofish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 9: Friendly Grouper (1-1)'); // Mutation
      bibleDetails.push('Kants Philosofish => Kants Philosofish'); // Breeding Preferred
      bibleDetails.push('Platos Philosofish => Blasphemous Angle Fish <br> Russells Philosofish => Nietzsches Philosofish <br> Nietzsches Philosofish => Yodelling Choirfish <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish'); // Breeding
      bibleDetails.push('all Grouper, all Catfish'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Nietzsches Philosofish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Day 5'); // Fertile
      bibleDetails.push('Day 17: 50% chance: dies, 10% chance: Invisible Piranha (1-1), 10% chance: Lesser Europan Shark (1-1), 10% chance: Recombinant Eel (school), 10% chance: Rainbow Sprat (school), 10% chance: Grey Sprat (school)'); // Mutation
      bibleDetails.push('Nietzsches Philosofish => Nietzsches Philosofish'); // Breeding Preferred
      bibleDetails.push('Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Lesser Europan Shark => Yodelling Choirfish <br> Greater Europan Shark => Yodelling Choirfish <br> Pan Europan Shark => Yodelling Choirfish <br> Coruscating Angelfish => Yodelling Choirfish <br> Blazing Angelfish => Yodelling Choirfish <br> Iridescent Angelfish => Yodelling Choirfish <br> Wailing Choirfish => Yodelling Choirfish <br> Yodelling Choirfish => Yodelling Choirfish <br> Siamese Catfish => Yodelling Choirfish <br> Manx Catfish => Yodelling Choirfish <br> Walking Bass => Yodelling Choirfish <br> Drummen Bass => Yodelling Choirfish <br> Double Bass => Yodelling Choirfish <br> Jovian Piranha => Yodelling Choirfish <br> Ionic Piranha => Yodelling Choirfish <br> Nano-Piranha => Yodelling Choirfish <br> Recombinant Eel => Yodelling Choirfish <br> Swarming Eel => Yodelling Choirfish <br> Parasitic Eel => Yodelling Choirfish <br> Piranha-eating Eel => Yodelling Choirfish <br> Acute Angle Fish => Yodelling Choirfish <br> Blasphemous Angle Fish => Yodelling Choirfish <br> Friendly Grouper => Yodelling Choirfish <br> Support Grouper => Yodelling Choirfish <br> Rock Grouper => Yodelling Choirfish <br> Legendary Grouper => Yodelling Choirfish <br> Platos Philosofish => Yodelling Choirfish <br> Russells Philosofish => Yodelling Choirfish <br> Kants Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('all Philosofish, all Europan Shark'); // Prey
      bibleDetails.push('30% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Platos Philosofish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 6: Right Angle Fish (1-1)'); // Mutation
      bibleDetails.push('Platos Philosofish => Platos Philosofish'); // Breeding Preferred
      bibleDetails.push('Russells Philosofish => Kants Philosofish <br> Kants Philosofish => Blasphemous Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish'); // Breeding
      bibleDetails.push('all Catfish, all Angle Fish'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Russells Philosofish') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 1'); // Fertile
      bibleDetails.push('Day 9: Acute Angle Fish (1-1)'); // Mutation
      bibleDetails.push('Russells Philosofish => Russells Philosofish'); // Breeding Preferred
      bibleDetails.push('Platos Philosofish => Kants Philosofish <br> Kants Philosofish => Nietzsches Philosofish <br> Nietzsches Philosofish => Yodelling Choirfish <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish'); // Breeding
      bibleDetails.push('all Catfish, all Eel'); // Prey
      bibleDetails.push('10% of body weight'); // Hunger
      bibleDetails.push('Largest suitable prey'); // Eating Style
    }
    if (fishName === 'Invisible Piranha') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('No'); // Buy from AliFEx
      bibleDetails.push('Sterile'); // Fertile
      bibleDetails.push('Day 17: 50% chance: dies, 10% chance: Nietzsches Philosofish (1-1), 10% chance: Schrodingers Catfish (school), 10% chance: Bermuda Tri-Angle Fish (school), 10% chance: Pan Europan Shark (school), 10% chance: Rainbow Sprat (1-1)'); // Mutation
      bibleDetails.push(''); // Breeding Preferred
      bibleDetails.push('Sterile'); // Breeding
      bibleDetails.push('all Sprat, all Piranha, all Philosofish, all Grouper, all Europan Shark, all Eel, all Choirfish, all Catfish, all Bass, all Angle Fish, all Angelfish'); // Prey
      bibleDetails.push('80% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Ionic Piranha') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 6'); // Fertile
      bibleDetails.push('Day 8: dies'); // Mutation
      bibleDetails.push('Ionic Piranha => Nano-Piranha'); // Breeding Preferred
      bibleDetails.push('Whistling Choirfish => Recombinant Eel <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('all Sprat, all Piranha, all Philosofish, all Grouper, all Europan Shark, all Eel, all Choirfish, all Catfish, all Bass, all Angle Fish, all Angelfish'); // Prey
      bibleDetails.push('80% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Jovian Piranha') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 25'); // Fertile
      bibleDetails.push('Day 46: dies'); // Mutation
      bibleDetails.push('Jovian Piranha => Ionic Piranha'); // Breeding Preferred
      bibleDetails.push('Drummen Bass => Atomic Eel <br> Siamese Catfish => Russells Philosofish <br> Manx Catfish => Russells Philosofish <br> Schrodingers Catfish => Russells Philosofish <br> Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('all Sprat, all Piranha, all Philosofish, all Grouper, all Europan Shark, all Eel, all Choirfish, all Catfish, all Bass, all Angle Fish, all Angelfish'); // Prey
      bibleDetails.push('80% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    if (fishName === 'Nano-Piranha') {
      bibleDetails.push(fishName); // Name of fish
      bibleDetails.push('Yes'); // Buy from AliFEx
      bibleDetails.push('Day 4'); // Fertile
      bibleDetails.push('Day 7: dies'); // Mutation
      bibleDetails.push('Nano-Piranha => Invisible Piranha'); // Breeding Preferred
      bibleDetails.push('Wailing Choirfish => Whistling Choirfish <br> Right Angle Fish => Right Angle Fish <br> Nietzsches Philosofish => Yodelling Choirfish'); // Breeding
      bibleDetails.push('all Sprat, all Piranha, all Philosofish, all Grouper, all Europan Shark, all Eel, all Choirfish, all Catfish, all Bass, all Angle Fish, all Angelfish'); // Prey
      bibleDetails.push('80% of body weight'); // Hunger
      bibleDetails.push('Any suitable prey'); // Eating Style
    }
    return bibleDetails;
  },
};

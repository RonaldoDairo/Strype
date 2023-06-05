<script>
import { loadStripe } from "@stripe/stripe-js"
import {onMount} from "svelte";
import axios from "axios";


let stripe  = null;
let cardElement = null;


onMount(()=>{
    loadStripeElements();

})
async function loadStripeElements(){
stripe = await loadStripe("pk_test_51NFGMvC5UXN5nuNS1bUdcmpKFVvvfVsI4cO4kZ5CUJYbreOGg3pgJCQZCxNK4bRbd69avZiIL6FCqBD0pPUNpRHz00owdxuhjw");

//  CREAR INSTANCIA DE LOS ELEMENTOS
let elements = stripe.elements();
let style = {
      base: {
        color: "#32325d",
        fontFamily:
          '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
          color: "#aab7c4",
        },
      },
      invalid: {
        color: "#fa755a",
      },
    };

    cardElement = elements.create("card", { style: style });

    cardElement.mount("#card-id");
  }

const submitPaymentMethod = async (e)=>{
        e.preventDefault();

        const payload = await stripe.createPaymentMethod({
            type : "card",
            card : cardElement,
        });
        console.log(payload,"paylo")


        if (payload.error){
            console.log(payload.error);
        }else{
            axios({
                url: "http://localhost:5000/payment/card",
                method: "POST",
                data: {
                    id: payload.paymentMethod.id,
                    description: "Razer Electra V2",
                    amount: 70 * 100
                }
            })
        }
};




</script>

<div>
    <div class="center-card">
      <form>
        <div class="card">
          <img
            src="https://i0.wp.com/www.pcmgames.com/wp-content/uploads/2018/06/Razer-Electra-V2-An%C3%A1lisis-ID.jpg?fit=1920%2C1080&ssl=1"
            alt=""
            class="img-card"
          />
          <h3>Razer Electra V2</h3>
          <p>$70 USD</p>
          <br />
          <div class="margin-card">
            <div id="card-id" />
          </div>
          <br />
          <button class="btn-payment" on:click={(e) => submitPaymentMethod(e)}>
            Comprar
          </button>
        </div>
      </form>
    </div>
  </div>
  
  <style>
    .center-card {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 5%;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
        Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
        "Segoe UI Symbol";
      text-align: center;
    }
    .card {
      width: 450px;
      height: 450px;
      -webkit-box-shadow: 3px 1px 15px 5px rgba(0, 0, 0, 0.12);
      box-shadow: 3px 1px 15px 5px rgba(0, 0, 0, 0.12);
    }
    .img-card {
      width: 100%;
      height: 250px;
    }
    .btn-payment {
      display: inline-block;
      font-weight: 400;
      height: 40px;
      width: 90%;
      text-align: center;
      vertical-align: middle;
      border: 1px solid transparent;
      font-size: 1rem;
      line-height: 1.5;
      /* BORDER RADIUS */
      border-radius: 5px;
      cursor: pointer;
      margin-left: 10px;
      margin-right: 10px;
      transition: 0.3s;
    }
    .btn-payment:hover {
      transition: 0.3s;
      background: #03045e;
      color: white;
    }
    .margin-card {
      margin-left: 10px;
      margin-right: 10px;
    }
  </style>
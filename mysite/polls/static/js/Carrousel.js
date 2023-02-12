'use Strict'

const grande    = document.querySelector('.Big')
const punto     = document.querySelectorAll('.punto')
let inicio    = -28.25
punto.forEach( (cadaPunto, i)=>{
    punto[i].addEventListener('click',()=>{

        let position = i
        let operacion = position * -50
        let ahora 

        //grande.style.transform = 'translateX('+ operacion +'%)';
        if (position==2){
            ahora = inicio - 100/14
            if (ahora > -95){
            grande.style.transform = 'translateX('+ ahora +'%)';
            inicio = ahora
            }
        }else if(position ==0){
            ahora = inicio + 100/14
            if (ahora < 45){
                grande.style.transform = 'translateX('+ ahora +'%)';
                inicio = ahora
            }
        }else{
            inicio = -28.25
            grande.style.transform = 'translateX('+inicio+'%)';
            
        }

punto.forEach(( cadaPunto, i)=>{
            punto[i].classList.remove('activo')

        })
        punto[i].classList.add('activo')
    
    
    })
})
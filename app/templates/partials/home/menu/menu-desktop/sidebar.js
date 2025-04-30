import Alpine from "alpinejs";

const sidebarControl = () => ({
  isOpen: true
  // init() {
  //   // Verificar se há estado salvo no localStorage
  //   const savedState = localStorage.getItem('sidebarState');
  //   if (savedState !== null) {
  //     this.isOpen = JSON.parse(savedState);
  //     // Sincronizar com o store global (quando disponível)
  //     if (Alpine.store) {
  //       Alpine.store('sidebar', { isOpen: this.isOpen });
  //     }
  //     // Aplicar classe no body imediatamente no carregamento
  //     document.body.classList.toggle('sidebar-collapsed', !this.isOpen);
  //   }
    
    // // Observar mudanças no estado da sidebar
    // this.$watch('isOpen', (value) => {
    //   // Atualizar store global (quando disponível)
    //   if (Alpine.store) {
    //     Alpine.store('sidebar', { isOpen: value });
    //   }
    //   // Salvar estado no localStorage
    //   localStorage.setItem('sidebarState', JSON.stringify(value));
    //   // Atualizar classe no body
    //   document.body.classList.toggle('sidebar-collapsed', !value);
    // });
  // }
});

Alpine.data("sidebarControl", sidebarControl);

// // Inicializar o store global quando o Alpine estiver pronto
// document.addEventListener('alpine:init', () => {
//   // Criar o store global para comunicação entre componentes
//   Alpine.store('sidebar', {
//     isOpen: true
//   });
// });
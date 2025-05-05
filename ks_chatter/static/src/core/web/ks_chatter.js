/** @odoo-module */

import { Chatter } from "@mail/chatter/web_portal/chatter";
import { patch } from "@web/core/utils/patch";
import { rpc } from "@web/core/network/rpc";
import { useService } from "@web/core/utils/hooks";
import {  onWillStart, onWillUpdateProps, onMounted, useState, useEffect, Component, useRef,onPatched, } from "@odoo/owl";
import { Thread } from "@mail/core/common/thread";
import { threadActionsRegistry } from "@mail/core/common/thread_actions";
import { FormController } from '@web/views/form/form_controller';
import { FormStatusIndicator } from "@web/views/form/form_status_indicator/form_status_indicator";
import { browser } from "@web/core/browser/browser";


patch(Chatter.prototype, {



    setup(){
        super.setup();
        this.state = useState({
                    // duration is expected to be given in minutes
                    current_record: [],
                    current_model: [],
                    current_model_records: [],
                    models: [],
                });
        this.threadService = useService("mail.store");
        useEffect(() => {
        this.willStart();
            }, () => [this.props.webRecord._initialTextValues])

        onWillUpdateProps(async (nextProps) => {
            if (this.props.webRecord._initialTextValues?.name == nextProps.webRecord._initialTextValues?.name){
                await this.willStart()
            }


        });
        onWillStart(()=> this.willStart())

        },

      async willStart() {
        let self = this;
        let ks_data = await rpc("/get/partner/models", {
                    model: this.props.threadModel,
                    id: this.props.threadId,
                    });
        this.props.data = ks_data;
        this.state.current_model = ks_data['current_model'];
        this.state.current_record = ks_data['current_record'];
        this.state.current_model_records = ks_data['current_model_records'];
        this.state.models = ks_data['models'];

      },

      async onModelChange(ev){
        var id=false;
        var selected_model = ev.target.value.split(',')[0];
        if (!this.props.data) {
            await this.willStart();
        }
        if(this.props.threadModel == selected_model){
            id=this.props.threadId;
        }
        else if(this.props.data[selected_model]){
            this.state.current_record = this.props.data[selected_model][0];
        }
        let ks_data = await rpc("/get/model/record", {
                    model: selected_model,
                    name: this.state.current_record,
                    id: id,
                    });
        if(this.props.threadModel == selected_model){
            this.state.current_record = ks_data['name'];
        }
        this.state.current_model = selected_model;
        this.state.current_model_records = this.props.data[selected_model];
        this.state.models = this.props.data['models'];
        console.log(ev);
        this.state.thread= this.threadService.Thread.insert({ model: selected_model, id: ks_data['id'] })

        this.changeThread(selected_model, ks_data['id'], this.webRecord);
                this.load(this.state.thread, this.requestList);

        const { messages: rawMessages } = await rpc('/mail/thread/messages', {
                'thread_id': ks_data['id'], 'thread_model': selected_model,
                limit: 30,
            });
        const messages = this.threadService.store.Message.insert(rawMessages.reverse(), { html: true });
        this.state.thread.fetchNewMessages();

      },

      async onRecordChange(ev){
            var selected_record = ev.target.value;
            var selected_model = this.state.current_model;
            let ks_data = await rpc("/get/record", {
                model: this.state.current_model,
                name: selected_record,
            });

            if(this.props.threadModel == selected_model){
            this.state.current_record = ks_data['name'];
        }
        this.state.current_record = selected_record.split(",");
        this.state.thread= this.threadService.Thread.insert({ model: selected_model, id: ks_data['id'] })
        this.changeThread(selected_model, ks_data['id'], this.webRecord);
                this.load(this.state.thread, this.requestList);

        const { messages: rawMessages } = await rpc('/mail/thread/messages', {
                'thread_id': ks_data['id'], 'thread_model': selected_model,
                limit: 30,
            });
        const messages = this.threadService.store.Message.insert(rawMessages.reverse(), { html: true });
        this.state.thread.fetchNewMessages(this.state.thread);

      },


})


